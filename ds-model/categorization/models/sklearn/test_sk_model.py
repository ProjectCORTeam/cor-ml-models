"""Test fasttext model."""
from pathlib import Path
from categorization.models.sklearn.sk_models import Categorizer

TEST_PATH = Path(__file__).resolve().parents[0]


class TestSKLearn_Categorizer_Model:
    """Test Scikit Learn Categorizer Model."""

    def setup(self):
        """Setup."""
        self.X = ['Fone de Ouvido Supra Auricular Com Microfone Bluetooth JBL T450',
                  'Mini System Lg 1800W Cd: Mini System Lg 1800W Cd',
                  'Tv Led 32 Sony Kdl32R305B Hd 2 Hdmi 1 USB Preta Com Conversor',
                  'Controle Js063 USB Para Xbox 360 E Pc - Multilaser',
                  'Café Expresso Café Do Centro Sul De Minas 10 Cápsula',
                  'Cappuccino Sabor Chocolate Nescafé Classic 200 g',
                  'Café Expresso Suplicy Torra Clara Em Cápsulas 10 Unidades',
                  'Café Expresso Suplicy Orgânico Em Cápsulas 10 Unidades']
        self.y = ['33697.0__33699.0', '33697.0__33699.0',
                  '33697.0__33699.0', '33697.0__33699.0',
                  '5742.0__5767.0', '5742.0__5767.0',
                  '5742.0__5767.0', '5742.0__5767.0']
        self.feats = ['Smartphone Lg G6 Lgh870.Abrabk 32 GB Platinum 4G Tela 5.7 Câme.',
                      'Café Marata Soluvel Sachet 50 g: Café Marata Soluvel Sachet 50 g']
        self.labels = ['33697.0__33699.0', '5742.0__5767.0']

    def test_model_predict(self):
        """Predict model test."""
        self.setup()
        model = Categorizer()
        model.fit(self.X, self.y)
        preds = list(model.predict(self.feats))
        assert self.labels == preds
