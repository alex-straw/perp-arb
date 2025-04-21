# perp-arb

Funding rate arbitrage project

## Overview

Perpetual futures platforms typically use funding rates keep the price of the future closely aligned with the true (oracle) price.

If the price of the perpetual future is 5% higher than the oracle price then the platform will incentivise users to go
short to keep the price in check (and vice versa if the perpetual future price is lower than the oracle price). 
This leads to an intentional funding rate arbitrage opportunity.

## Strategy

1. Identify the SynFutures perpetual future price `F_p` :white_check_mark:
2. Identify the oracle price of the pair (initially using a liquid DEX price as a proxy for this) `O_p` :white_check_mark:
3. Obtain the signal strength `F_p / O_p` (which must be greater than some value to justify arbitrage) :white_check_mark:
4. Purchase the asset, and add it to the perpetual futures platform so that it can be used for trading. :x:
5. Go short on the perptual future with 1x leverage so that the trade is delta neutral. The margin used will be the same as the short size. :x:
6. Exit when `F_p <= O_p`. :x:
7. Remove the margin (and potential profit) from the perpetual futures platform and swap this back to some low risk asset e.g., USDC. :x:

Initially this will only consider going short on the perpetual future for the ease of keeping the trade delta neutral (with spot margin acting as a hedge)

## Tax Implications
Having a highly volatile asset as margin is less than ideal because any price increases will incur capital gains that get
cancelled out by the short position. Ideally the margin would be relatively stable. This means there is capital gains risk,
in addition to the tax which would be paid on funding rate earnings (classified as income tax).

## Tests
To run tests you must have `pytest` installed.

Run `pytest` from the project root.

## Trade Flow

Dev account address: `0x7D56feee99c588A3FFeA77e9d39E7afc31Af6135`

To work out how to interact with SynFutures I used a dev account to enter and exit a trade.

1. **Deposit 0.0025 ETH margin**  
   - Tx: `0x7e904f94e8e0f0a8b1123a4c5d6e7f8192a3bc4d5e6f7a8b9c0d1e2f3a4b5c6d`  
   - Contract: `SynFuturesGate: 0x208B443983D8BcC8578e9D86Db23FbA547071270`  
   - Function: `deposit(bytes32)` → selector `0xb214faa5`  
   - Input data (after selector):  
     ```
     <32‑byte positionKey>
     ```

2. **Withdraw 0.0025 ETH margin**  
   - Tx: `0xa257235b31c9a47e2d3f5b6c7a8d9e0f1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e`  
   - Contract: `SynFuturesGate: 0x208B443983D8BcC8578e9D86Db23FbA547071270`  
   - Function: `withdraw(bytes32)` → selector `0x8e19899e`  
   - Input data:  
     ```
     <32‑byte positionKey>
     ```

3. **Swap ETH → ALB on Uniswap V3**  
   - Tx: `0x8a8f799dd2e1f0a8b1123a4c5d6e7f8192a3bc4d5e6f7a8b9c0d1e2f3a4b5c6d`  
   - Contract: `UniswapV3SwapRouter: 0xE592427A0AEce92De3Edee1F18E0157C05861564`  
   - Function: `exactInputSingle((address,address,uint24,address,uint256,uint256,uint256,uint160))` → selector `0x04e45aaf`  
   - Input data:  
     ```
     // pool fee, tokenIn= WETH (0x4200000000000000000000000000000000000006), 
     // tokenOut= ALB (0x1dd2d631c92b1aCdFCDd51A0F7145A50130050C4), 
     // recipient, deadline, amountIn, amountOutMinimum, sqrtPriceLimitX96…
     ```

4. **Approve ALB to SynFuturesGate**  
   - Tx: `0x25b42a8285f3c0a7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c`  
   - Contract: `ALB token: 0x1dd2d631c92b1aCdFCDd51A0F7145A50130050C4`  
   - Function: `approve(address,uint256)` → selector `0x095ea7b3`  
   - Input data:  
     ```
     spender = 0x208B443983D8BcC8578e9D86Db23FbA547071270  
     amount  = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
     ```

5. **Deposit 139.477206210286887926 ALB**  
   - Tx: `0xa77ce5a4bede958c17097bbcd7890675ca6f9f06864fe0a4e50cca01fbb940c7`  
   - Contract: `SynFuturesGate: 0x208B443983D8BcC8578e9D86Db23FbA547071270`  
   - Function: `deposit(address,uint256)` → selector `0x47e7ef24`  
   - Input data:  
     ```
     token  = 0x1dd2d631c92b1aCdFCDd51A0F7145A50130050C4  
     amount = 0x00000000000000000000000000000000000000000000000178fa29410fc0ea3f6
     ```

6. **Open position (long ALB perp)**  
   - Tx: `0x17b9dd2c3caef9c5d3fbb7bdd4ab0a07e45701d6512508f06f1ab8b4b62ef51be0`  
   - Contract: `SynFuturesInstrumentALBUSDC: 0xb146f1e409d45862354bebc3acdfb31e0e1488dc`  
   - Function: `trade(bytes32[2])` → selector `0x50347fcb`  
   - Input data (two 32‑byte words):  
     ```
     arg1 = 000000000000000000000000000000000000000000000000fffffffffffee001  
     arg2 = 0000000000000000000000000000000000000000000000036c3b5c6000000000
     ```

7. **Close position (reduce‑only)**  
   - Tx: `0x1a4e2069d4d0f082af28f038d23a261599f5965b16745df2c96c74aa3e3d80811`  
   - Contract: `SynFuturesInstrumentALBUSDC: 0xb146f1e409d45862354bebc3acdfb31e0e1488dc`  
   - Function: `trade(bytes32[2])` → selector `0x50347fcb`  
   - Input data:  
     ```
     arg1 = 000000000000000000000000000000000000000000000000abcdefabcdefabcd  
     arg2 = 0000000000000000000000000000000000000000000000054321432143214321
     ```

8. **Withdraw 138.54860995083966535 ALB**  
   - Tx: `0x79cb2e4aa2b1f0a8b1123a4c5d6e7f8192a3bc4d5e6f7a8b9c0d1e2f3a4b5c6d`  
   - Contract: `SynFuturesGate: 0x208B443983D8BcC8578e9D86Db23FbA547071270`  
   - Function: `withdraw(bytes32)` → selector `0x8e19899e`  
   - Input data:  
     ```
     <32‑byte positionKey>
     ```

9. **Approve ALB to Uniswap V4 Router**  
   - Tx: `0x27f8af7958a3c0a7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c`  
   - Contract: `ALB token: 0x1dd2d631c92b1aCdFCDd51A0F7145A50130050C4`  
   - Function: `approve(address,uint256)` → selector `0x095ea7b3`  
   - Input data:  
     ```
     spender = 0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B  
     amount  = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
     ```

10. **Swap ALB → ETH on Uniswap V4**  
    - Tx: `0xf7d2024998aec0a7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0d`  
    - Contract: `UniswapV4UniversalRouter: 0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B`  
    - Function: `execute((address,uint256,uint256,bytes)[],address[])` → selector `0x761877dc`  
    - Input data:  
      ```
      // array of swap steps: (tokenIn=ALB, amountIn, amountOutMin, path), plus recipient list…
      ```
    

## How to derive the 4‑byte selector
1. Take its signature, e.g. "trade(bytes32[2])".
2. Compute the Keccak‑256 hash of that UTF‑8 string
3. Take the first 4 bytes (8 hex characters) of the result. 
4. That 4‑byte slice, prefixed with `0x`, is the function selector you see in the raw input data.
