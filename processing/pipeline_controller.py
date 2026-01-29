# # from processing.cleaning.clean_transactions import clean_transactions
# # from processing.harmonization.curate_transactions import curate_transactions
# # from processing.quality.enforce_contracts import (
# #     enforce_clean_contract,
# #     enforce_curated_contract
# # )

# # def run_processing_pipeline(raw_df):
# #     try:
# #         clean_df = clean_transactions(raw_df)
# #         clean_df = enforce_clean_contract(clean_df)

# #         curated_df = curate_transactions(clean_df)
# #         curated_df = enforce_curated_contract(curated_df)

# #         return curated_df

# #     except Exception as e:
# #         raise RuntimeError(f"Pipeline failed due to data quality issue: {str(e)}")


# # PHASE ALPHA CODE 
# from utils.logger import get_logger
# logger = get_logger(__name__)

# def run_processing_pipeline(raw_df):
#     try:
#         logger.info("Starting cleaning stage")
#         clean_df = clean_transactions(raw_df)
#         clean_df = enforce_clean_contract(clean_df)

#         logger.info("Starting curation stage")
#         curated_df = curate_transactions(clean_df)
#         curated_df = enforce_curated_contract(curated_df)

#         logger.info("Pipeline completed successfully")
#         return curated_df

#     except Exception as e:
#         logger.error(f"Pipeline failed: {str(e)}")
#         raise


# Phase BETA CODE 
from utils.logger import get_logger

from processing.cleaning.clean_transactions import clean_transactions
from processing.harmonization.curate_transactions import curate_transactions
from processing.quality.enforce_contracts import (
    enforce_clean_contract,
    enforce_curated_contract
)

logger = get_logger(__name__)

def run_processing_pipeline(raw_df):
    try:
        logger.info("Starting cleaning stage")
        clean_df = clean_transactions(raw_df)
        clean_df = enforce_clean_contract(clean_df)

        logger.info("Starting curation stage")
        curated_df = curate_transactions(clean_df)
        curated_df = enforce_curated_contract(curated_df)

        logger.info("Pipeline completed successfully")
        return curated_df

    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
        raise
