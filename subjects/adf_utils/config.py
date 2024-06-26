class new_census:
    """
    Configuration of dataset Survey Census Income
    """

    # the size of total features
    params = 10

    input_bounds = []
    input_bounds.append([17, 99])
    input_bounds.append([1, 8])
    input_bounds.append([1, 24])
    input_bounds.append([1, 5])
    input_bounds.append([10, 9830])
    input_bounds.append([1, 554])
    input_bounds.append([0, 17])
    input_bounds.append([1, 2])
    input_bounds.append([1, 9])
    input_bounds.append([1, 1])

    # the name of each feature
    feature_name = ["AGEP", "COW", "SCHL", "MAR", "OCCP", "POBP", "RELP", "WKHP", "SEX", "RAC1P"]

    # the name of each class
    class_name = ["low", "high"]

    # specify the categorical features with their indices
    categorical_features = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# adapted from ADF https://github.com/pxzhang94/adf
class census:
    """
    Configuration of dataset Census Income
    """

    # the size of total features
    params = 13

    input_bounds = []
    input_bounds.append([1, 9])
    input_bounds.append([0, 7])
    input_bounds.append([0, 39]) #69 for THEMIS
    input_bounds.append([0, 15])
    input_bounds.append([0, 6])
    input_bounds.append([0, 13])
    input_bounds.append([0, 5])
    input_bounds.append([0, 4])
    input_bounds.append([0, 1])
    input_bounds.append([0, 99])
    input_bounds.append([0, 39])
    input_bounds.append([0, 99])
    input_bounds.append([0, 39])

    # the name of each feature
    feature_name = ["age", "workclass", "fnlwgt", "education", "marital_status", "occupation", "relationship", "race", "sex", "capital_gain",
                                                                      "capital_loss", "hours_per_week", "native_country"]

    # the name of each class
    class_name = ["low", "high"]

    # specify the categorical features with their indices
    categorical_features = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

class credit:
    """
    Configuration of dataset German Credit
    """

    # the size of total features
    # note that for feature 9 (gender): 1,3,4 are male (replaced with 0) and 2.5 are female (replace with 1)
    params = 20

    input_bounds = []
    input_bounds.append([1, 4])
    input_bounds.append([4, 72])
    input_bounds.append([0, 4])
    input_bounds.append([0, 10])
    input_bounds.append([250, 18424])
    input_bounds.append([1, 5])
    input_bounds.append([1, 5])
    input_bounds.append([1, 4])
    input_bounds.append([0, 1])
    input_bounds.append([1, 3])
    input_bounds.append([1, 4])
    input_bounds.append([1, 4])
    input_bounds.append([19, 75])
    input_bounds.append([1, 3])
    input_bounds.append([1, 3])
    input_bounds.append([1, 4])
    input_bounds.append([1, 4])
    input_bounds.append([1, 2])
    input_bounds.append([1, 2])
    input_bounds.append([1, 2])

    # the name of each feature
    feature_name = ["checking_status", "duration", "credit_history", "purpose", "credit_amount", "savings_status", "employment", "installment_commitment", "sex", "other_parties",
                    "residence", "property_magnitude", "age", "other_payment_plans", "housing", "existing_credits", "job", "num_dependents", "own_telephone", "foreign_worker"]

    # the name of each class
    class_name = ["bad", "good"]

    # specify the categorical features with their indices
    categorical_features = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19]

class bank:
    """
    Configuration of dataset Bank Marketing
    """

    # the size of total features
    params = 16

    input_bounds = []
    input_bounds.append([1, 9])
    input_bounds.append([0, 11])
    input_bounds.append([0, 2])
    input_bounds.append([0, 3])
    input_bounds.append([0, 1])
    input_bounds.append([-20, 179])
    input_bounds.append([0, 1])
    input_bounds.append([0, 1])
    input_bounds.append([0, 2])
    input_bounds.append([1, 31])
    input_bounds.append([0, 11])
    input_bounds.append([0, 99])
    input_bounds.append([1, 63])
    input_bounds.append([-1, 39])
    input_bounds.append([0, 1])
    input_bounds.append([0, 3])

    # the name of each feature
    feature_name = ["age", "job", "marital", "education", "default", "balance", "housing", "loan", "contact", "day",
                                                                      "month", "duration", "campaign", "pdays", "previous", "poutcome"]

    # the name of each class
    class_name = ["no", "yes"]

    # specify the categorical features with their indices
    categorical_features = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

class compas:
    """
    Configuration of dataset Compas
    """

    # the size of total features
    params = 12

    input_bounds = []
    input_bounds.append([0, 1])
    input_bounds.append([0, 2])
    input_bounds.append([0, 1])
    input_bounds.append([0, 20])
    input_bounds.append([1, 10])
    input_bounds.append([0, 38])
    input_bounds.append([0, 1])
    input_bounds.append([0, 1])
    input_bounds.append([0, 1])
    input_bounds.append([1, 10])
    input_bounds.append([1, 10])
    input_bounds.append([0, 38])

    # the name of each feature
    feature_name = []

    # the name of each class
    class_name = ["no", "yes"]

    # specify the categorical features with their indices
    categorical_features = [0, 1, 2, 4, 6, 7, 8, 9, 10]
