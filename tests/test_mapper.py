import unittest

SAMPLE_DB = [
    {"brand": "Glycomet-GP 2", "salt": "Glimepiride 2mg + Metformin 500mg", "brand_mrp": 245, "janaushadhi_mrp": 48},
    {"brand": "Telma 40", "salt": "Telmisartan 40mg", "brand_mrp": 220, "janaushadhi_mrp": 36},
    {"brand": "Augmentin 625 Duo", "salt": "Amoxycillin 500mg + Clavulanic Acid 125mg", "brand_mrp": 223, "janaushadhi_mrp": 62}
]

def calculate_savings(items):
    b_total = sum(i["brand_mrp"] for i in items)
    g_total = sum(i["janaushadhi_mrp"] for i in items)
    saved = b_total - g_total
    pct = round((saved / b_total) * 100)
    return b_total, g_total, saved, pct

class TestSwasthyaSetuEngine(unittest.TestCase):
    def test_cost_savings_calculation(self):
        b_total, g_total, saved, pct = calculate_savings(SAMPLE_DB)
        self.assertEqual(b_total, 688)
        self.assertEqual(g_total, 146)
        self.assertEqual(saved, 542)
        self.assertEqual(pct, 79)

    def test_salt_integrity(self):
        for item in SAMPLE_DB:
            self.assertTrue(len(item["salt"]) > 0)
            self.assertLess(item["janaushadhi_mrp"], item["brand_mrp"])

if __name__ == "__main__":
    unittest.main()
