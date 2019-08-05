import pytest
from app.opiniones_parser import OpinionesParser

def test_should_fail_if_file_not_found():
    with pytest.raises(FileNotFoundError):
        parser = OpinionesParser('archivo_falso.csv')
