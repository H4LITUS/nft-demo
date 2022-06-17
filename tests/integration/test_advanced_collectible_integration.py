from aiohttp import request
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONEMNTS,
    get_account,
    get_contract,
)
from brownie import network
import pytest
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import get_account
import time


def test_can_create_advanced_collectible_integration():
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONEMNTS:
        pytest.skip()

    # Act
    advanced_collectible, creation_tx = deploy_and_create()
    time.sleep(60)

    # Assert
    assert advanced_collectible.tokenCounter() == 1
