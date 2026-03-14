# FLOW_NODE_WORK_HOURS_COMPARISON.md

## Comparison of Work Hours Across Versions and Node Types

This table summarizes differences in reported annual work hours for each node type, explains the assumptions behind them, and clarifies why discrepancies exist.

| Node Type    | Version | Annual Hours | Hours per Person per Year | Assumptions / Notes |
|-------------|---------|-------------|--------------------------|-------------------|
| Urban (500 m²) | v2.0 protein model | 486 | 0.97 | High automation (Level 3), only active cultivation tasks counted (harvest, monitoring, minimal maintenance). |
| Peri-urban (2 ha) | v2.0 protein model | 870 | 1.74 | Semi-automated (Level 2), includes agroforestry maintenance (planting, pruning, harvesting). |
| Regional (1 000 m²) | v2.0 protein model | 200 | 0.4 | High-tech crops (spirulina, lentils, mung beans), fully automated (Level 4), only active cultivation tasks. |
| **Total** | v2.0 protein model | 1,556 | 3.1 | Minimal tasks included; extreme automation assumed. |

| Node Type    | Latest CAPEX/OPEX version | Annual Hours | Hours per Person per Year | Assumptions / Notes |
|-------------|--------------------------|-------------|--------------------------|-------------------|
| Urban (500 m²) | CAPEX/OPEX v1 | 1,000 | 2 | Includes cultivation + energy system maintenance, minor administration, small problem-solving. |
| Peri-urban (2 ha) | CAPEX/OPEX v1 | 1,200 | 2.4 | Includes agroforestry work, irrigation adjustments, monitoring, admin, training. |
| Regional (1 000 m²) | CAPEX/OPEX v1 | 2,000 | 4 | Fully automated crops, plus energy system operation, storage monitoring, minor human intervention. |
| **Total** | CAPEX/OPEX v1 | 4,200 | 8.4 | Comprehensive hours including all operational, administrative, and maintenance tasks. |

### Key Observations

1. **Automation Level Impact**  
   - Level 3–4 automation drastically reduces active cultivation hours.  
   - Realistic operational workload (CAPEX/OPEX version) includes additional tasks beyond cultivation.

2. **Scope of Counting**  
   - Protein model version: only active farming tasks.  
   - CAPEX/OPEX version: active farming + energy maintenance + admin + small operational tasks.

3. **Node Type Considerations**  
   - Urban: small area, high-value crops → low total hours in both versions.  
   - Peri-urban: land-intensive → moderate hours, more human involvement in agroforestry.  
   - Regional: large, high-energy crops → higher total hours even with automation.

4. **Conclusion**  
   - Discrepancy arises from **different definitions of “work”** and **inclusion of associated maintenance and operational tasks**.  
   - For real-world planning, the CAPEX/OPEX hours are more realistic.  
   - Extreme low-hour estimates are achievable **only under perfect automation** and minimal interventions.

---

**Recommendation:** Use CAPEX/OPEX hours for financial and staffing planning, and keep the protein-model hours as a benchmark for **ideal automation efficiency**.
