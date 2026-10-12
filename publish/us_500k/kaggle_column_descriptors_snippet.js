(function() {
  const descriptions = {
  "transaction_id": "Transaction identifier: TX_ + zero-padded 8-digit sequence, shared by all six views",
  "card_id": "Card token: CARD_ + zero-padded 6-digit sequence",
  "pan_masked": "Masked Primary Account Number (BIN + ****** + last 4 digits)",
  "product_id": "Card product tier, e.g. PROD_REWARDS_SIGNATURE, PROD_CHECKING_DEBIT, PROD_TOKENIZED_DPAN",
  "cohort_id": "Cardholder demographic and behavioral cohort ID",
  "merchant_id": "Unique merchant entity identifier",
  "merchant_name": "Commercial trading name of the merchant",
  "mid": "Merchant Identification Number: MID_ + acquirer BIN + zero-padded terminal sequence",
  "tid": "Terminal Identification Number: TID_ + zero-padded 4-digit sequence",
  "mcc": "Merchant Category Code (ISO 18245, 4 digits)",
  "merchant_category": "Merchant category label, e.g. Grocery / Supermarket, Restaurants / Dining, Quasi-Cash / Crypto On-Ramp",
  "merchant_lat": "Latitude coordinate of merchant location in decimal degrees",
  "merchant_lon": "Longitude coordinate of merchant location in decimal degrees",
  "acquirer_bin": "Bank Identification Number of acquiring bank",
  "gateway_provider": "Payment gateway routing provider",
  "country_code": "ISO 3166-1 alpha-2 country code of transaction location",
  "postal_code": "Postal/ZIP code of merchant or terminal location",
  "timestamp_utc": "ISO 8601 UTC timestamp of transaction authorization",
  "tx_time_seconds": "Elapsed simulation time in seconds from epoch start",
  "hour_of_day": "Local wall-clock hour of transaction arrival (0 to 23)",
  "day_of_week": "Day of the week (0 = Monday, 6 = Sunday)",
  "amount": "Transaction currency amount in major units (USD)",
  "amount_minor": "Transaction currency amount in minor units (integer cents)",
  "currency": "ISO 4217 three-letter currency code (USD)",
  "channel_type": "Transaction channel: CP_POS_CHIP, CP_POS_CONTACTLESS, CNP_WEB, or CNP_MOBILE",
  "credit_limit": "Assigned credit line ceiling in major units (USD)",
  "current_balance": "Current ledger balance on the account in major units (USD)",
  "available_balance": "Available credit balance remaining in major units (USD)",
  "user_avg_tx_amount_30d": "Welford rolling mean of card transaction amount over 30 days",
  "user_std_tx_amount_30d": "Welford rolling standard deviation of amount over 30 days",
  "z_score_amount_30d": "Standard score of current transaction amount vs 30-day baseline",
  "tx_count_1h": "Count of authorized transactions on card in past 1 hour",
  "tx_count_24h": "Count of authorized transactions on card in past 24 hours",
  "tx_attempts_1h": "Count of all transaction attempts (incl. declines) in past 1 hour",
  "distinct_mids_30m": "Count of distinct MIDs attempted on card in past 30 minutes",
  "subminute_attempts_60s": "Count of rapid velocity attempts on card within 60 seconds",
  "tx_amount_sum_24h": "Cumulative spend on card in past 24 hours (USD)",
  "distinct_merchants_24h": "Count of distinct merchants transacted with in past 24 hours",
  "distance_from_last_tx_km": "Haversine distance in kilometers from previous transaction location",
  "time_since_last_tx_seconds": "Time elapsed in seconds since previous transaction on card",
  "haversine_velocity_kph": "Apparent travel velocity required between successive transactions (km/h)",
  "ip_distance_from_home_km": "Geodetic distance in km between client IP and cardholder billing address",
  "client_ip": "Client IPv4 address recorded at transaction gateway",
  "asn_type": "Client network classification: residential, mobile, or datacenter",
  "geo_risk_score": "Geospatial velocity/anomaly band as an integer 0-95 (0 = no elevation)",
  "device_canvas_hash": "Browser canvas fingerprint hash for web transactions (null for CP)",
  "is_cross_border": "Boolean flag indicating whether transaction crossed country borders",
  "billing_shipping_match": "Address-verification match between billing and shipping; encoded 1 match, 0 mismatch",
  "avs_match_code": "Address Verification Service result code (Y, A, Z, N, U)",
  "cvv_match_flag": "CVV check result: 1 match, 0 no match",
  "is_fraud": "Ground-truth fraud label: 1 fraudulent, 0 legitimate",
  "scenario_tag": "Traffic class: ORGANIC_NORMAL, HARD_NEGATIVE_{TRAVEL,RELOCATION,EMERGENCY}, or INTENT_OMEGA_{PROBE,HARVEST,BISECT_DRAIN}",
  "syndicate_id": "Adversarial syndicate identifier; populated for fraud rows only",
  "botnet_cluster_id": "Automated botnet cluster identifier; populated for a subset of rows",
  "mule_ring_id": "Money-mule ring identifier; populated for fraud rows only",
  "beneficiary_account_id": "Beneficiary account token receiving liquidated funds; populated for fraud rows only",
  "ip_subnet_prefix": "Client IP /24 subnet routing prefix",
  "device_fingerprint_id": "Unique client hardware device fingerprint ID",
  "risk_score": "Composite heuristic fraud risk score computed by BankDecisionEngine (0.0 to 1.0)",
  "base_risk": "Ex-ante risk prior to behavioral escalation; constant 0.002 across this export",
  "dominant_causal_driver": "Primary Structural Causal Model factor explaining transaction risk escalation",
  "analytical_shapley_probability": "Exact Pearlian SCM Shapley attribution vector in probability delta space",
  "analytical_shapley_log_odds": "Exact Pearlian SCM Shapley attribution vector in log-odds logit space",
  "counterfactual_input_deltas": "Minimal intervention input deltas required to flip bank decision",
  "counterfactual_mode": "Target state of counterfactual twin: approve or decline",
  "counterfactual_twin": "Complete counterfactual transaction twin JSON under abduction-action-prediction",
  "normative_baseline": "Cardholder normative spending baseline reference vector",
  "explanation_narrative": "Human-readable causal explanation generated from ground-truth Shapley attributions",
  "mti": "ISO 8583 Message Type Identifier; 0100 (Authorization Request) throughout this export",
  "stan": "Systems Trace Audit Number (6-digit ISO 8583 field 11)",
  "rrn": "Retrieval Reference Number (12-digit ISO 8583 field 37)",
  "auth_code": "Authorization approval code (6-character alphanumeric ISO 8583 field 38)",
  "response_code": "ISO 8583 authorization response code; observed set 00, 10, 51, 57, 59, 63, 65, 82",
  "auth_response_code": "ISO 8583 field 39 authorization response code; same observed set as response_code",
  "pos_entry_mode": "ISO 8583 POS entry mode: 051 chip, 071 contactless, 012 card-not-present web, 102 card-not-present mobile",
  "pos_condition_code": "ISO 8583 POS condition code; 00 normal, 59 e-commerce",
  "eci": "Electronic Commerce Indicator (e.g. 05 3DS authenticated, 07 non-3DS)",
  "trans_status_3ds": "EMV 3-D Secure authentication status: Y (authenticated), N (failed), C (challenge required)",
  "vaai_score": "Visa Advanced Authorization network risk score, integer 0-98 in this export",
  "hop_origin": "Originating hop server or ingestion edge node identifier",
  "clearing_mti": "ISO 8583 clearing message type identifier: 0200 (Financial Presentment)",
  "clearing_delay_hours": "Latency in hours between real-time authorization and clearing batch settlement",
  "settled_amount": "Final presentment settlement amount in major currency units (USD)",
  "settled_amount_minor": "Final presentment settlement amount in integer cents",
  "interchange_fee_minor": "Card scheme interchange assessment fee in integer cents",
  "hawkes_intensity_R": "Real-time self-exciting Hawkes process intensity state on card account",
  "asn": "Autonomous System Number of the client network gateway, AS-prefixed (e.g. AS7018); empty for most rows",
  "isp": "Internet Service Provider operating client IP network",
  "ja4_signature": "JA4 TLS client fingerprint signature",
  "mule_tier": "Liquidation tier: TIER_1_SMURF, TIER_2_AGGREGATOR, or TIER_3_OFFRAMP; empty for non-fraud rows",
  "liquidation_channel": "Cash-out rail: INSTANT_P2P_SMURF, SECONDARY_GIFT_CARD_P2P, SAME_DAY_ACH_CONSOLIDATION, ACH_KITING_WHOLESALE, or BINANCE_BYBIT_P2P_USDT_TRC20; empty for non-fraud rows"
};

  const sortedKeys = Object.keys(descriptions).sort((a, b) => b.length - a.length);
  const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;

  // Find all description inputs
  const inputs = Array.from(document.querySelectorAll('input')).filter(inp => {
    const ph = (inp.placeholder || '').toLowerCase();
    return ph.includes('enter') || ph.includes('description');
  });

  console.log(`Found ${inputs.length} description input boxes.`);

  let filled = 0;
  inputs.forEach(input => {
    let p = input.parentElement;
    let matchedCol = null;

    // Walk up until we reach the cell container holding the column header label
    while (p && p !== document.body && !matchedCol) {
      const text = p.innerText || p.textContent || '';
      for (const col of sortedKeys) {
        const re = new RegExp('\\b' + col + '\\b');
        if (re.test(text)) {
          matchedCol = col;
          break;
        }
      }
      if (!matchedCol) {
        p = p.parentElement;
      }
    }

    if (matchedCol && descriptions[matchedCol]) {
      nativeSetter.call(input, descriptions[matchedCol]);
      input.dispatchEvent(new Event('input', { bubbles: true }));
      input.dispatchEvent(new Event('change', { bubbles: true }));
      filled++;
      console.log(`[${filled}] Matched ${matchedCol}`);
    }
  });

  console.log(`COMPLETE: Successfully filled ${filled} of ${inputs.length} columns! Now click the black Save button.`);
})();
