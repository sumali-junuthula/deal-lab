def calculate_accretion(buyer_eps, target_eps, synergy, deal_ratio):
  combined_eps = buyer_eps + (target_eps * deal_ratio) + synergy
  accretion_pct = ((combined_eps - buyer_eps) / buyer_eps) * 100

  return {
    "combined_eps": round(combined_eps, 2),
    "accretion_pct": round(accretion_pct, 2),
    "status": "accretive" if accretion_pct > 0 else "dilutive"
  }
