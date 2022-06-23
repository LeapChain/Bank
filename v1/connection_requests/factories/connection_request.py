from leapchain.constants.network import BANK, CONFIRMATION_VALIDATOR
from leapchain.factories.network_node import NetworkNodeFactory
from leapchain.factories.network_validator import NetworkValidatorFactory


class BankConnectionRequestFactory(NetworkNodeFactory):
    node_type = BANK


class ValidatorConnectionRequestFactory(NetworkValidatorFactory):
    node_type = CONFIRMATION_VALIDATOR
