# SwasthyaSetu AI (स्वास्थ्यसेतु AI)
**Vernacular Prescription Reader, Generic Drug Mapper & Welfare Triage**  
*Built for Hack for Social Cause – Youth Tech Challenge 2027 (VBYLD 2027) in partnership with IIT Bombay.*

## 1. Overview & Problem Context
Over 65% of out-of-pocket health expenditure in India is spent on medicines. Low-income families in Uttar Pradesh (Varanasi) and Delhi face complex English prescriptions and expensive branded medicines, unaware that CDSCO-verified **Pradhan Mantri Bhartiya Janaushadhi Pariyojana (PMBJP)** generic equivalents cost 50%–80% less.

**SwasthyaSetu AI** scans prescriptions, extracts active pharmaceutical salts, computes exact Jan Aushadhi cost savings, reads dosage schedules aloud in **Hindi & Bhojpuri**, and checks **Ayushman Bharat (PM-JAY)** welfare eligibility.

## 2. Quick Setup Steps
```bash
# 1. Clone the repository
git clone [https://github.com/YOUR-USERNAME/SwasthyaSetu-AI.git](https://github.com/YOUR-USERNAME/SwasthyaSetu-AI.git)
cd SwasthyaSetu-AI

# 2. Configure Environment Variables
cp .env.example .env

# 3. Launch the Prototype
# Option A: Open index.html directly in Chrome/Edge for instant client-side & offline-ready demo
# Option B: Serve locally via Python HTTP server
python3 -m http.server 8080
