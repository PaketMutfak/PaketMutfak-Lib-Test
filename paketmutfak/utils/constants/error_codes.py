class MessageCode:
    UNEXPECTED_ERROR_ON_SERVICE_MESSAGE = 1
    WORKING_HOURS_FORMAT_ERROR_MESSAGE = 2
    MISSING_DATA_ERROR_MESSAGE = 3
    UNKNOWN_MANAGER_ERROR_MESSAGE = 4
    BUILDING_NOT_FOUND_ERROR_MESSAGE = 5
    BRAND_NOT_FOUND_ERROR_MESSAGE = 6
    DATA_FORMAT_ERROR_MESSAGE = 7
    COMPLETED_MESSAGE = 8
    WRONG_DATA_ERROR_MESSAGE = 9
    UNAUTHORAZATION_ERROR_MESSAGE = 10
    MISSING_TOKEN_ERROR_MESSAGE = 11
    MEMBER_NOT_FOUND_ERROR_MESSAGE = 12
    KITCHEN_NOT_FOUND_ERROR_MESSAGE = 13
    ORDER_INTO_ANOTHER_BASKET = 14
    ORDER_NOT_FOUND = 15
    INVALID_BASKET_STATUS = 16
    BASKET_NOT_FOUND = 17
    ORDER_STATUS_NOT_UPDATE_ON_PLATFORMS = 18
    ORDER_NOT_IN_BASKET = 19
    COURIER_NOT_FOUND = 20
    BASKET_NO_COURIER = 21
    BASKET_STATUS_NO_AVAILABLE_DELIVERED = 22
    BASKET_STATUS_NO_AVAILABLE_COMPLETED = 23
    ORDER_STATUS_ALREADY_UPDATED = 24
    CLIENT_DATA_ERROR = 25
    DUPLICATE_BUILDING_NAME_ERROR = 26
    DUPLICATE_PHONE_NUMBER_ERROR = 27
    DUPLICATE_BUILDING_ADDRESS_ERROR = 28
    TR_IDENTITY_NUMBER_ERROR = 29
    DUPLICATE_TR_IDENTITY_NUMBER_ERROR = 30
    MIN_BASKET_PRICE_ERROR = 31
    MAX_AND_MIN_DELIVERY_TIME_ERROR_1 = 32
    MAX_AND_MIN_DELIVERY_TIME_ERROR_2 = 33
    MAX_AND_MIN_DELIVERY_TIME_ERROR_3 = 34
    EMAIL_FORMAT_ERROR = 35
    DUPLICATE_EMAIL_ERROR = 36
    DUPLICATE_BRAND_NAME_ERROR = 37
    DUPLICATE_MEMBER_TAX_NUMBER_ERROR = 38
    DUPLICATE_MEMBER_NAME_ERROR = 39
    BRAND_ALREADY_ADDED_TO_BUILDING_ERROR = 40
    PHONE_NUMBER_FORMAT_ERROR = 41
    INVALID_COURIER_STATUS = 42
    ASSIGN_MORE_THAN_ONE_BASKET_ERROR = 43
    COURIER_HAS_BASKET_ERROR = 44
    COURIER_CONTRACT_TYPE_ERROR = 45
    NO_COORDINATES_FOR_BASKET_ERROR = 46
    DUPLICATE_USER_ID_ERROR = 47
    USER_NOT_FOUND_ERROR_MESSAGE = 48
    INVALID_ORDER_TYPE_ERROR = 49
    INVALID_RESTAURANT_STATUS_ERROR = 50
    RATE_LIMITER_ERROR = 51
    CLOSE_OPEN_RESTAURANT_NOT_WORK_ERROR_MESSAGE = 52
    BRAND_LOG_NOT_INSERTED_ERROR_MESSAGE = 53
    ADISYON_NOT_FOUND = 54
    MAX_LIMIT_BASKET_ORDER_COUNT = 55
    BASKET_CREATED_SUCCESS = 56
    ORDER_STATUS_UPDATED_SUCCESS = 57
    BASKET_REMOVED_SUCCESS = 58
    ORDER_ASSIGN_COURIER_SUCCESS = 59
    INVALID_END_OF_DAY_STATUS = 60
    ORDER_REMOVED_BASKET_SUCCESS = 61
    ADISYON_CANCELLED_SUCCESS = 62
    YS_INTEGRATED_ERROR = 63
    CANCEL_ADISYON_NO_REASON_ERROR = 64
    PRICE_FORMAT_ERROR = 65
    START_END_DATE_ERROR = 66
    PERAKENDE_PRICE_LIMIT_ERROR = 67
    PAYMENT_DISCREPANCY_ERROR = 68
    UPDATE_REGIONS_STATUS_ERROR = 69
    OTM_NOT_FOUND = 70
    DATE_FORMAT_ERROR = 71
    OTM_ALREADY_ACTIVATED = 72
    REGION_NOT_FOUND = 73
    ADDRESS_NOT_FOUND = 74
    DUPLICATE_REGION_NAME = 75
    PLATFORM_NOT_FOUND = 76
    DUPLICATE_BRAND_ERROR = 77
    DUPLICATE_OTM_NAME_ERROR = 78
    SERVICE_TIME_UPDATE_ERROR = 79
    TY_INTEGRATED_ERROR = 80
    GT_INTEGRATED_ERROR = 81
    ORDER_CANCEL_REASON_ERROR = 82
    INVALID_ORDER_STATUS = 83
    INVALID_RESTAURANT_COURIER_STATUS = 84
    COURIER_NOT_ASSIGN_ERROR = 85
    DISCOUNT_PRICE_BIGGER_THAN_TOTAL = 86
    PLATFORM_INTEGRATION_ERROR = 87
    REMOVE_PLATFORM_INTEGRATION_ERROR = 88
    INVALID_ROLE_TYPE = 89
    INVALID_SERVICE_NAME = 90
    INVALID_USER_NAME_OR_PASSWORD = 91
    MULTIPLE_USER_NAME = 92
    CREATE_USERNAME_SERVICE_ERROR = 93
    BRAND_PLATFORM_INTEGRATION_PROBLEM = 94
    PROBLEM_HEALTH_PROBLEM = 95
    ORDER_FORMATTING_ERROR = 96
    INVALID_TOKEN_ERROR = 97
    BRAND_MENU_ALREADY_CREATED = 98
    PRODUCT_NOT_FOUND = 99
    PRODUCT_ALREADY_MATCHED = 100
    PRODUCT_PLATFORM_ERROR = 101
    DUPLICATE_PLATFORM_ERROR = 102
    DELETE_ALL_MEMBERS_IN_OTM_ERROR = 103
    DELETE_ALL_REGIONS_IN_OTM_ERROR = 104
    DELETE_ALL_PLATFORM_IN_OTM_ERROR = 105
    PHONE_NUMBER_AND_ROLE_ID_MATCH_ERROR = 106
    WRONG_EMAIL_ADDRESS = 107
    WRONG_OTP_FORMAT = 108
    EXPIRED_OTP_CODE = 109
    INVALID_OTP_CODE = 110
    LAST_PASSWORD_ERROR = 111
    INVALID_MOBILE_DEVICE = 112
    NO_DEVICE_MATCH_WITH_COURIER = 113
    PLATFORM_INTEGRATION_UPDATE_ERROR = 114
    NOT_FOUND_COURIERS_BY_PARAMS = 115
    NOT_FOUND_COORDINATES_BY_PARAMS = 116
    NOT_FOUND_ORDERS_BY_PARAMS = 117
    NOT_FOUND_COURIER_OPS_BY_PARAMS = 118
    INACTIVE_PAYMENT_METHOD = 119


class MysqlErrorCode:
    MYSQL_DUPLICATE_ENTRY_ERROR_CODE = 1062
    MYSQL_FOREIGN_KEY_CONSTRAINT_FAILS_ERROR_CODE = 1452
    MYSQL_CONSTRAINT_FAILS_ERROR_CODE = 3819
