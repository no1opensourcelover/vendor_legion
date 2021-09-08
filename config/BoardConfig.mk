# Safetynet
TARGET_FORCE_BUILD_FINGERPRINT := google/barbet/barbet:11/RD2A.210905.002/7513089:user/release-keys

# Namespace for fwk-detect
TARGET_FWK_DETECT_PATH ?= hardware/qcom-caf/common
PRODUCT_SOONG_NAMESPACES += \
    $(TARGET_FWK_DETECT_PATH)/fwk-detect
