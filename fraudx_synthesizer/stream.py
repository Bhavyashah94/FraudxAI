"""Real-time streaming daemon for FraudX-Synthesizer.

Provides high-throughput transaction streaming to REST endpoints or stdout
with zero PRISM-X coupling, asynchronous dispatch, and deterministic replaying.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
import urllib.request
import urllib.error
from typing import Any, Dict, Optional, Tuple

from .engine import SimulationEngine


async def dispatch_transaction_async(
    endpoint: str,
    record: Dict[str, Any],
    timeout_sec: float = 2.0,
) -> Tuple[bool, int, float]:
    """Asynchronously dispatches a JSON transaction payload to a target REST endpoint."""
    loop = asyncio.get_running_loop()
    payload = json.dumps(record).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    t0 = time.perf_counter()

    def _sync_post():
        try:
            with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
                return True, resp.status
        except urllib.error.HTTPError as e:
            return False, e.code
        except Exception:
            return False, 0

    success, status_code = await loop.run_in_executor(None, _sync_post)
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    return success, status_code, elapsed_ms


async def run_stream_daemon(
    endpoint: Optional[str] = None,
    duration_sec: float = 60.0,
    target_tps: float = 5.0,
    fraud_prevalence: float = 0.02,
    seed: int = 42,
    to_stdout: bool = False,
) -> None:
    """Executes continuous streaming transaction emission loop."""
    engine = SimulationEngine(n_cards=500, n_merchants=100, seed=seed)
    print(
        f"[FraudX-Synthesizer Stream Daemon] Initialized (seed={seed}, target_tps={target_tps}, duration={duration_sec}s)",
        file=sys.stderr,
    )

    count = 0
    t_start = time.time()
    for record in engine.stream_continuous(
        duration_seconds=duration_sec,
        target_tps=target_tps,
        fraud_prevalence=fraud_prevalence,
    ):
        count += 1
        if to_stdout or endpoint is None:
            print(json.dumps(record))
            sys.stdout.flush()
        else:
            success, code, latency = await dispatch_transaction_async(endpoint, record)
            if not success:
                print(f"[WARN] Failed dispatch {record['transaction_id']} (HTTP {code})", file=sys.stderr)

        # Rate limiting sleep
        await asyncio.sleep(1.0 / max(target_tps, 0.1))

    total_time = time.time() - t_start
    print(
        f"[FraudX-Synthesizer Stream Daemon] Finished: {count} transactions in {total_time:.2f}s ({count / max(total_time, 0.01):.1f} TPS)",
        file=sys.stderr,
    )


def main():
    parser = argparse.ArgumentParser(description="FraudX-Synthesizer Streaming CLI")
    parser.add_argument("--endpoint", type=str, default=None, help="Target REST API URL (e.g. http://localhost:8000/api/v1/predict)")
    parser.add_argument("--duration", type=float, default=30.0, help="Stream duration in seconds")
    parser.add_argument("--tps", type=float, default=5.0, help="Target transactions per second")
    parser.add_argument("--fraud-rate", type=float, default=0.03, help="Adversarial fraud ratio (0.0 to 1.0)")
    parser.add_argument("--seed", type=int, default=42, help="Deterministic random seed")
    parser.add_argument("--stdout", action="store_true", help="Print transactions to stdout as JSON lines")

    args = parser.parse_args()
    asyncio.run(run_stream_daemon(
        endpoint=args.endpoint,
        duration_sec=args.duration,
        target_tps=args.tps,
        fraud_prevalence=args.fraud_rate,
        seed=args.seed,
        to_stdout=args.stdout,
    ))


if __name__ == "__main__":
    main()
