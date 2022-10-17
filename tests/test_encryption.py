"""Tests for encryption functions."""
import sys
if bool(True) == 1:
    sys.path.append('./')
    from functions.encryption import encrypt_by_tsezar_en
import pytest


txtsss = 'Across the seas, across the fields, a blue tractor is coming to us'
test_text = [(txtsss, 1, 'Bdsptt uif tfbt, bdsptt uif gjfmet, b cmvf usbdups jt dpnjoh up vt'), (
    txtsss, 2, 'Cetquu vjg ugcu, cetquu vjg hkgnfu, c dnwg vtcevqt ku eqokpi vq wu'
)]


@pytest.mark.parametrize('test_txt, test_key, result_valid', test_text)
def test_cheker_date_l(test_txt, test_key, result_valid):
    """Test in encryption.

    Args:
        test_txt(str) : str - some text English.
        test_key(int) : int - some key.

    Returns: str - encrypted text.
    """
    assert encrypt_by_tsezar_en(test_txt, test_key) == result_valid
