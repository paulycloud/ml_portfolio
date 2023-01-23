# WorldBank Health Dataset 

The dataset [`world_bank_health_population`](https://cloud.google.com/bigquery?sq=1057666841514:3bb229234d7f4b379098581f0101e923&_ga=2.81369303.-1379782407.1673021064&project=paulkamau&ws=!1m9!1m3!3m2!1sbigquery-public-data!2sworld_bank_health_population!1m4!4m3!1sbigquery-public-data!2sworld_bank_health_population!3scountry_series_definitions) combines key health statistics from a variety of sources to provide a look at global health and population trends. It includes information on nutrition, reproductive health, education, immunization, and diseases from over 200 countries from 1960 - 2020

Multiple tables have been used to compile the data. The data was flattened to create a single working set: 

- Country series definitions 
- Country summary 
- Health nutrition population
- International debt
- Series summary 
- Series times

See the Data operations file for the series of transformations. 

# Potential ML Models
## Logisitic Regression Models: 
- TBD

## Linear Regression Models: How to use a linear regression model to:
### averages
- Predict the average Total alcohol consumption per capita (SH.ALC.PCAP.LI) using the World Bank Health dataset in BigQuery ML `[SH_ALC_PCAP_LI,SH_PRV_SMOK_FE,SH_STA_DIAB_ZS,SH_PRV_SMOK_MA,SH_PRV_SMOK,SH_ALC_PCAP_FE_LI,SH_ALC_PCAP_MA_LI]`

- Predict the average age at first marriage for female (SP.DYN.SMAM.FE) using the World Bank Health dataset in BigQuery ML

- Predict the average age at first marriage for males (SP.DYN.SMAM.MA) using the World Bank Health dataset in BigQuery ML
`[SH_STA_PNVC_ZS,SH_PRG_SYPH_ZS,SH_MMR_RISK,SH_STA_ANVC_ZS,SP_M18_2024_FE_ZS,SP_DYN_SMAM_MA,SH_STA_BRTC_ZS,SH_MMR_WAGE_ZS,SH_STA_ANV4_ZS,SH_MMR_RISK_ZS,SH_VAC_TTNS_ZS,SP_UWT_TFRT,SP_DYN_WFRT,SP_MTR_1519_ZS,SP_DYN_CONU_ZS,SH_FPL_SATI_ZS,SP_DYN_CONM_ZS,SP_DYN_SMAM_FE,SH_STA_MMRT_NE,SH_MMR_DTHS,SH_FPL_SATM_ZS,SP_ADO_TFRT,SH_STA_MMRT,SP_M15_2024_FE_ZS]`

#### annual 
- Predict the Total alcohol consumption per capita (SH.ALC.PCAP.LI) for the US in 2020 using the World Bank Health dataset in BigQuery ML
- Predict the age at first marriage for female (SP.DYN.SMAM.FE) for the US in 2020 using the World Bank Health dataset in BigQuery ML
- Predict the age at first marriage for males (SP.DYN.SMAM.MA) for the US using the World Bank Health dataset in BigQuery ML

## K-Means Clustering Models: 
- TBD 

## Timeseries Models: 
- Predict the Total alcohol consumption per capita (SH.ALC.PCAP.LI) for the US in 2022 using the World Bank Health dataset in BigQuery ML
- Predict the age at first marriage for female (SP.DYN.SMAM.FE) for the US in 2022 using the World Bank Health dataset in BigQuery ML
- Predict the age at first marriage for males (SP.DYN.SMAM.MA) for the US using the World Bank Health dataset in BigQuery ML


## Matrix Factorization Models: 
- TBD


--------------------------------------------------------------------------------
_Let's connect and chat! Open to anyone on Earth under the Sun and Moon._
Find all my social links here

#### All My Links
[BioLink](https://bio.link/paulkamau)


#### Buy Me Coffee
[Cashapp](https://bio.link/paulkamau)
[PayPal](https://paypal.me/paulkamau)
