import pandas as pd
import pytest
from processing.quality.quality_rules import validate_positive_values

def test_validate_positive_values_raises_error():
    df = pd.DataFrame({"quantity": [1, -2]})

    with pytest.raises(ValueError):
        validate_positive_values(df, "quantity")
