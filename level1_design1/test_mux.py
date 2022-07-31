# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Develop your test here ########')
    
    for i in range (0, 31):
        dut.sel.value = random.randint (i, i) #asserting values to selection line from 0 to 30
        #cocotb.log.info(f'##### sel = {dut.sel.value} ########')
        dut.inp0.value= 3 if (i==0) else 0
        dut.inp1.value= 3 if (i==1) else 0
        dut.inp2.value= 3 if (i==2) else 0
        dut.inp3.value= 3 if (i==3) else 0
        dut.inp4.value= 3 if (i==4) else 0
        dut.inp5.value= 3 if (i==5) else 0
        dut.inp6.value= 3 if (i==6) else 0
        dut.inp7.value= 3 if (i==7) else 0
        dut.inp8.value= 3 if (i==8) else 0
        dut.inp9.value= 3 if (i==9) else 0
        dut.inp10.value= 3 if (i==10) else 0
        dut.inp11.value= 3 if (i==11) else 0
        dut.inp12.value= 3 if (i==12) else 0
        dut.inp13.value=3 if (i==13) else 0
        dut.inp14.value=3 if (i==14) else 0
        dut.inp15.value=3 if (i==15) else 0
        dut.inp16.value=3 if (i==16) else 0
        dut.inp17.value=3 if (i==17) else 0
        dut.inp18.value=3 if (i==18) else 0
        dut.inp19.value=3 if (i==19) else 0
        dut.inp20.value=3 if (i==20) else 0
        dut.inp21.value=3 if (i==21) else 0
        dut.inp22.value=3 if (i==22) else 0
        dut.inp23.value=3 if (i==23) else 0
        dut.inp24.value=3 if (i==24) else 0
        dut.inp25.value=3 if (i==25) else 0
        dut.inp26.value=3 if (i==26) else 0
        dut.inp27.value=3 if (i==27) else 0
        dut.inp28.value=3 if (i==28) else 0
        dut.inp29.value=3 if (i==29) else 0
        dut.inp30.value=3 if (i==30) else 0
        
        await Timer(2, units='ns')
        cocotb.log.info(f'##### sel = {dut.sel.value} ########')
        '''l = [dut.inp0.value, dut.inp1.value, dut.inp2.value, dut.inp3.value, dut.inp4.value, 
            dut.inp5.value, dut.inp6.value, dut.inp7.value, dut.inp8.value, dut.inp9.value, 
            dut.inp10.value, dut.inp11.value, dut.inp12.value, dut.inp13.value, dut.inp14.value, 
            dut.inp15.value, dut.inp16.value, dut.inp17.value, dut.inp18.value, dut.inp19.value, 
            dut.inp20.value, dut.inp21.value, dut.inp22.value, dut.inp23.value, dut.inp24.value, 
            dut.inp25.value, dut.inp26.value, dut.inp27.value, dut.inp28.value, dut.inp29.value, dut.inp30.value]'''
        dut._log.info(f'Sel={dut.sel.value}')
        dut._log.info(f'Inpt={dut.inp10}')
    assert dut.out.value==3, "Randomised test failed with: {Sel}".format(Sel=dut.sel.value)
