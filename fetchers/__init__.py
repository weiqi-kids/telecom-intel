"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .american_tower import AmericanTowerFetcher
from .att import AttFetcher
from .calix import CalixFetcher
from .ceragon import CeragonFetcher
from .chunghwa import ChunghwaFetcher
from .ciena import CienaFetcher
from .commscope import CommscopeFetcher
from .crown_castle import CrownCastleFetcher
from .deutsche_telekom import DeutscheTelekomFetcher
from .equinix import EquinixFetcher
from .ericsson import EricssonFetcher
from .fareastone import FareastoneFetcher
from .nokia import NokiaFetcher
from .sba_comm import SbaCommFetcher
from .softbank import SoftbankFetcher
from .taiwan_mobile import TaiwanMobileFetcher
from .tmobile import TmobileFetcher
from .verizon import VerizonFetcher
from .zte import ZteFetcher

FETCHERS = {
    "american_tower": AmericanTowerFetcher,
    "att": AttFetcher,
    "calix": CalixFetcher,
    "ceragon": CeragonFetcher,
    "chunghwa": ChunghwaFetcher,
    "ciena": CienaFetcher,
    "commscope": CommscopeFetcher,
    "crown_castle": CrownCastleFetcher,
    "deutsche_telekom": DeutscheTelekomFetcher,
    "equinix": EquinixFetcher,
    "ericsson": EricssonFetcher,
    "fareastone": FareastoneFetcher,
    "nokia": NokiaFetcher,
    "sba_comm": SbaCommFetcher,
    "softbank": SoftbankFetcher,
    "taiwan_mobile": TaiwanMobileFetcher,
    "tmobile": TmobileFetcher,
    "verizon": VerizonFetcher,
    "zte": ZteFetcher,
}
