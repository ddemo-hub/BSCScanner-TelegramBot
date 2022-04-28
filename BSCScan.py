from web3 import Web3
import re
import time
import Constants as keys

web3 = Web3(Web3.HTTPProvider(keys.BSC_NODE_PROVIDER))

def getLatestBlock():
    return web3.eth.blockNumber

def isHashValid(hash):
    if re.search("^0x([A-Fa-f0-9]{64})$", hash):
        return True
    else:
        return False
    
def getTransactionInfo(txnHash):
    if (isHashValid(txnHash)):
        info = web3.eth.get_transaction(txnHash) 
        infoTable = f"blockHash: {info['blockHash'].hex()}             \n\
                    \nblockNumber: {info['blockNumber']}               \n\
                    \nfrom: {info['from']}                             \n\
                    \nto: {info['to']}                                 \n\
                    \ngas: {info['gas']}                               \n\
                    \ngasPrice: {info['gasPrice']}                     \n\
                    \ninput: {info['input']}                           \n\
                    \nnonce: {info['nonce']}                           \n\
                    \ntransactionIndex: {info['transactionIndex']}     \n\
                    \nvalue: {info['value']}                           \n\
                    \ntype: {info['type']}                             \n\
                    \nv: {info['v']}                                   \n\
                    \nr: {info['r'].hex()}                             \n\
                    \ns: {info['s'].hex()}                               "
        return infoTable
    else:
        return "Geçersiz Hash Kodu"

def getTransactionCount(blockID):
    try:
        return web3.eth.get_block_transaction_count(blockID)
    except:
        return "Geçersiz Blok ID"

def transactionInInterval(timeConstraint):
    if timeConstraint < 3 or timeConstraint % 3 != 0:
        return "Zaman aralığının 3'ün katı olması önerilir"
    
    currentBlock = web3.eth.blockNumber
    while currentBlock == web3.eth.blockNumber:
        pass
    
    currentBlock = web3.eth.blockNumber 
    numberOfTransactions = web3.eth.get_block_transaction_count(currentBlock)
    
    t_end = time.time() + timeConstraint
    while time.time() < t_end:
        if currentBlock == web3.eth.blockNumber:
            pass
        elif currentBlock != web3.eth.blockNumber:
            currentBlock = web3.eth.blockNumber
            numberOfTransactions = numberOfTransactions + web3.eth.get_block_transaction_count(currentBlock)
    
    return numberOfTransactions    
