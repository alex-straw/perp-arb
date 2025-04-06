from src.models.data_models import ERC20DTO


def sqrt_price_x96_to_price_syn_futures(sqrt_price_x96: int, token0: ERC20DTO, token1: ERC20DTO, is_inverse=False, verbose=False) -> float:
    """
    Converts sqrtPriceX96 (sqrtPriceX96 = sqrt(token1/token0) * 2**96) to the actual price of token0 per token1.

    SynFutures sqrt_price_x96 does not need adjusting for decimals (no actual token transfer)
    """

    if sqrt_price_x96 <= 0:
        raise ValueError(f"sqrt_price_x96 must be > 0 but was {sqrt_price_x96}")

    if token0.address >= token1.address:
        raise ValueError(f"token0 {token0.name} address must be less than token1 {token1.name} address.")

    price = _sqrt_price_x96_to_raw_price(sqrt_price_x96)

    if is_inverse:
        price = 1/price

    if verbose:
        print(f"{token0.name.value}/{token1.name.value} = {price:.8f}")

    return price


def sqrt_price_x96_to_price(sqrt_price_x96: int, token0: ERC20DTO, token1: ERC20DTO, verbose=False) -> float:
    """
    Converts sqrtPriceX96 (sqrtPriceX96 = sqrt(token1/token0) * 2**96) to the actual price of token1 per token0.
    Assumes token0.address < token1.address.
    Adjusts for decimals: price = token1 / token0
    """

    if sqrt_price_x96 <= 0:
        raise ValueError(f"sqrt_price_x96 must be > 0 but was {sqrt_price_x96}")

    if token0.address >= token1.address:
        raise ValueError(f"token0 {token0.name} address must be less than token1 {token1.name} address.")

    price = _sqrt_price_x96_to_raw_price(sqrt_price_x96) * (10 ** (token0.decimals - token1.decimals))

    if verbose:
        print(f"{token0.name.value}/{token1.name.value} = {price:.8f}")

    return price


def _sqrt_price_x96_to_raw_price(sqrt_price_x96: int):
    return (sqrt_price_x96 ** 2) / (2 ** 192)
