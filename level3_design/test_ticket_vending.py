# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.Clock, 10, units="us")  # Create a 10us period clock on port Clock
    cocotb.start_soon(clock.start())        # Start the clock

    # Clear
    dut.Clear.value = 1
    await FallingEdge(dut.Clock)  
    dut.Clear.value = 0
    await FallingEdge(dut.Clock)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    
    #inp_seq = [1, 1, 0, 1, 1, 1]
    inp_seq = [1, 1, 0, 1, 0, 1, 1, 1]
    
    await RisingEdge(dut.Clock)
    for i in range (0, len(inp_seq), 2):
        cocotb.log.info("----------------------")
        await Timer(3, units="us")
        dut.Ten.value = inp_seq[i]
        dut.Twenty.value = inp_seq[i+1]
        cocotb.log.info(f"Output bit Ready = {dut.Ready.value}")
        cocotb.log.info(f"Output bit Dispense = {dut.Dispense.value}")
        cocotb.log.info(f"Output bit Return = {dut.Return.value}")
        cocotb.log.info(f"Output bit Bill = {dut.Bill.value}")
        await RisingEdge(dut.Clock)
        cocotb.log.info(f"Ten = {dut.Ten.value}")
        cocotb.log.info(f"Ten = {dut.Twenty.value}")
        cocotb.log.info(f"Current state = {dut.State.value}")
        cocotb.log.info(f"Next state = {dut.NextState.value}")
        
    #assert dut.seq_seen.value==1, f"Failed testcase for input sequence {inp_seq}"
