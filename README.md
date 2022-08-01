# challenges-Chaitanya27111
challenges-Chaitanya27111 created by GitHub Classroom

# Level1_Design1
Image of gitpod environment with id
![image](https://user-images.githubusercontent.com/84698480/182023520-0dd18eb0-6264-409d-91f8-a5b25dbb1b2c.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in a 4 bit selection line input *sel* and 31 inputs each of 2 bits *inp0_31* and outputs 2 bit *out*

The values are assigned to the input port using 
```
dut.sel.value = random.randint (i, i) 
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
```

The assert statement is used for comparing the mux's output to the expected value.

The following error is seen:
```
assert dut.out.value==3, "Randomised test failed with: sel = {Sel} \nExpected output = {eout}  Received output = {dval}".format(Sel=dut.sel.value, eout=ou, dval=dut.out.value)
                     AssertionError: Randomised test failed with: sel = 01100 
                     Expected output = 3  Received output = 00
```
## Test Scenario **(Important)**
- Test Inputs: sel=01100 inp12=11 remaining inputs (inp0-30 except 12 = 00)
- Expected Output: sum=11
- Observed Output in the DUT dut.out=00

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 begin
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12; // bug===>missed sel=01100, modify it to 5'b01100: out = inp12;
      5'b01101: out = inp13; 
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29; // no selection lines for line 30, hence sel=11110 will give 0 as output
      default: out = 0;
    endcase
```
Here, the case statement pertaining to the case of selection line *sel*=01101 has been written twice and the case of *sel*=01100 has been missed out

## Design Fix
Update the case of inp12 from ```5'b01101: out = inp12; ```to ```5'b01100: out = inp12;```
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/84698480/182025652-54c412bc-8312-4f43-bea2-d2e0fb66014e.png)

The bug is fixed in the same file mux.v and has been highlighted by a comment
![image](https://user-images.githubusercontent.com/84698480/182026071-4fc61b49-f8cb-42b6-9f1e-885ead991d62.png)

## Verification Strategy
Here the design has 31*2(inp) + 4(sel) input bits, hence the exhaustive testing would consume  much time. To overcome this, Only the input which has to be selected by the selection line inputs *sel* has
been assigned value 11 and remaining inputs are asigned a value of 00. If the design is bug free, it will yield output as 11 for all inputs of selection line except 11110 
as that will fall under default case.

## Is the verification complete ?
Yes



# Level1_Design2
Image of gitpod environment with id
![image](https://user-images.githubusercontent.com/84698480/182100357-2f9cb50c-6ee9-456c-abea-9f278f48763f.png)

# State Diagram
![state diag](https://user-images.githubusercontent.com/84698480/182130452-fb4ce95f-7636-4a96-a6e9-a0584efd1a39.jpg)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes 
1 bit *inp_bit*, 1 bit *reset* and *clk* as inputs and outputs a single bit value *seq_seen*.

The values are assigned to the input port using 

### Testcase1
```
inp_seq = [1, 1, 0, 1, 1, 1]
await RisingEdge(dut.clk)
for i in range (0, len(inp_seq)):
        cocotb.log.info("----------------------")
        await Timer(3, units="us")
        dut.inp_bit.value = inp_seq[i]
        cocotb.log.info(f"Output bit = {dut.seq_seen.value}")
        await RisingEdge(dut.clk)
        cocotb.log.info(f"Input bit = {dut.inp_bit.value}")
        cocotb.log.info(f"Current state = {dut.current_state.value}")
        cocotb.log.info(f"Next state = {dut.next_state.value}")
```

The assert statement is used for comparing the sequence detector's output with expected output.

The following error is seen:
```
assert dut.seq_seen.value==1, f"Failed testcase for input sequence {inp_seq}"
                     AssertionError: Failed testcase for input sequence [1, 1, 0, 1, 1, 1]
```
![image](https://user-images.githubusercontent.com/84698480/182125772-2bd52fc7-5be2-475c-b52d-2002cd512c90.png)


## Test Scenario1 **(Important)**
- Test Inputs: sequence of *inp_bit*=110111, initially the *reset* is made high till one falling edge and then made low
- Expected Output: *seq_seen*=1
- Observed Output in the DUT *seq_seen*=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug1
Based on the above test input, and inspecting the output log, it is found that the next state after the state *SEQ_1* when an input bit 1 is encountered is *IDLE*.
However, the next state must actually be *SEQ_1*
```
#from line 46 of seq_detect_1011.v
 SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE; // bug===>next state must be SEQ_1
        else
          next_state = SEQ_10;
      end
```

## Design Fix1
Update the value assigned to *next_state* from *IDLE* to *SEQ_1* when *inp_bit* is 1 as shown below
```
#from line 46 of seq_detect_1011.v
 SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1; // bug found here has been fixed
        else
          next_state = SEQ_10;
      end
```

Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/84698480/182123047-ad4275be-4e97-4362-bf51-537f82590819.png)

The bug is fixed in the same file seq_detect_1011.v and has been highlighted by a comment
![image](https://user-images.githubusercontent.com/84698480/182123316-d343c2bc-86fe-4034-b661-851b95cb5407.png)



## Test Scenario2 **(Important)**
- Test Inputs: sequence of *inp_bit*=11010111, initially the *reset* is made high till one falling edge and then made low
- Expected Output: *seq_seen*=1
- Observed Output in the DUT *seq_seen*=0

Output mismatches for the above inputs proving that there is a design bug

### Testcase2
```
inp_seq = [1, 1, 0, 1, 0, 1, 1, 1]
await RisingEdge(dut.clk)
for i in range (0, len(inp_seq)):
        cocotb.log.info("----------------------")
        await Timer(3, units="us")
        dut.inp_bit.value = inp_seq[i]
        cocotb.log.info(f"Output bit = {dut.seq_seen.value}")
        await RisingEdge(dut.clk)
        cocotb.log.info(f"Input bit = {dut.inp_bit.value}")
        cocotb.log.info(f"Current state = {dut.current_state.value}")
        cocotb.log.info(f"Next state = {dut.next_state.value}")
```

The assert statement is used for comparing the sequence detector's output with expected output.

The following error is seen:
```
assert dut.seq_seen.value==1, f"Failed testcase for input sequence {inp_seq}"
                     AssertionError: Failed testcase for input sequence inp_seq = [1, 1, 0, 1, 0, 1, 1, 1]
```
![image](https://user-images.githubusercontent.com/84698480/182126786-d3b602c2-d2e4-418e-952e-4d9729bcdf51.png)


## Design Bug2
Based on the above test input, and inspecting the output log, it is found that the next state after the state *SEQ_101* when an input bit 1 is encountered is *IDLE*.
However, the next state must actually be *SEQ_10*
```
#from line 62f seq_detect_1011.v
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE; //bug===>next state must be SEQ_10
      end
```

## Design Fix2
Update the value assigned to *next_state* from *IDLE* to *SEQ_10* when *inp_bit* is 1 as shown below
```
#from line 62 of seq_detect_1011.v
 SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
        /**************Bug fix start**************/
          next_state = SEQ_10; //bug found here has been fixed
        /**************Bug fix end**************/
      end
```

Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/84698480/182127987-32b2f64d-f993-4e87-8c5c-c6c6a8669d66.png)

The bug is fixed in the same file seq_detect_1011.v and has been highlighted by a comment
![image](https://user-images.githubusercontent.com/84698480/182128044-9d903602-4fe0-4b60-a84d-da251f82abb8.png)


## Verification Strategy
Various corner cases have been thought of and have been applied to the DUT. The inputs are asserted values using for loop. In such a verification methodolgy, understanding of design and its working are really important.

## Note
For detection of overlapping sequence, the next state after *SEQ_1011* must be *SEQ_10* in case when *inp_bit* is 0 and *SEQ_1* when *inp_bit* is 1. However, this has been not considered as a bug as of now. (Considering that this has been done willingly by the designer)



# Level3_Design
Image of gitpod environment with id
![image](https://user-images.githubusercontent.com/84698480/182178097-c99f56bc-2e70-476a-b1b3-cc5c57099fec.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes 
1 bit *Ten*, 1 bit *Twenty* and *Clock* as inputs and outputs *Dispense*, *Return*, *Bill* and *Ready* each of 1 bit.

The values are assigned to the input port using 

### Testcase
```
    # Clear
    dut.Clear.value = 1
    await FallingEdge(dut.Clock)  
    dut.Clear.value = 0
    await FallingEdge(dut.Clock)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    
    inp_seq = [1, 0, 0, 1, 1, 0] # $10+$20+$10 = $40
    
    await RisingEdge(dut.Clock)
    for i in range (0, len(inp_seq), 2):
        cocotb.log.info("----------------------")
        dut.Ten.value = inp_seq[i]
        dut.Twenty.value = inp_seq[i+1]
        await RisingEdge(dut.Clock)
```

The assert statement is used for comparing the sequence detector's output with expected output.

The following error is seen:
```
assert dut.Dispense.value==1, f"Failed testcase for input sequence {inp_seq}"
                     AssertionError: Failed testcase for input sequence [1, 0, 0, 1, 1, 0]
```
![image](https://user-images.githubusercontent.com/84698480/182179209-d8597bca-28e9-418b-8e4d-75a9fc6b0e66.png)


## Test Scenario **(Important)**
- Test Inputs: sequence of *inp_bit*=100110, initially the *Clear* is made high till one falling edge and then made low to reset the machine
here, each pair of bits represents {Ten, Twenty} dollar bill inserted in the machine i.e.
10_01_10 = 3 bills inserted
           1st bill of $10
           2nd bill of $20
           3rd bill of $10
- Expected Output: *Dispense*=1
As the sum of the bill inserted is $40, the ticket must be dispensed by the machine.
- Observed Output in the DUT *Dispense*=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug introduced
The next state from current state *BILL10* has been changed to *BILL20* when the inserted bill is of $20
```
#from line 123 of ticket_vending.v
 BILL10:	begin
		if (Ten)
			NextState = BILL20;
		else if (Twenty)
			//NextState = BILL30;
			NextState = BILL20; //bug introduced
		else
			NextState = BILL10;
		end
```

## Design Fix

```
#from line 123 of seq_detect_1011.v
 BILL10:	begin
		if (Ten)
			NextState = BILL20;
		else if (Twenty)
			NextState = BILL30;   // resolved
			//NextState = BILL20; //bug introduced
		else
			NextState = BILL10;
		end
```

Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/84698480/182123047-ad4275be-4e97-4362-bf51-537f82590819.png)

The bug is fixed in the same file seq_detect_1011.v and has been highlighted by a comment
![image](https://user-images.githubusercontent.com/84698480/182180943-3a618fd4-e031-49eb-a5a4-fdacc9477207.png)


## Verification Strategy
Various corner cases have been thought of and have been applied to the DUT. The inputs are asserted values using for loop. In such a verification methodolgy, understanding of design and its working are really important.



# Level2_Design

# Bit Manipulation Processor Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![image](https://user-images.githubusercontent.com/84698480/182200024-df8b3a80-afc0-411e-b358-bb787d5848da.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 3 source operands *mav_putvalue_src1*, *mav_putvalue_src2*, *mav_putvalue_src3* and 1 instruction code *mav_putvalue_instr* each of 32 bits.

The values are assigned to the input port using 
```
mav_putvalue_src1 = 0x5
mav_putvalue_src2 = 0x1
mav_putvalue_src3 = 0x2
mav_putvalue_instr = 0x101010B3
```

The assert statement is used for comparing the bitmanipulator's output to the expected value.

The following error is seen:
```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0xa does not match MODEL = 0x0
```
## Test Scenario **(Important)**
- Test Inputs: 
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x2
    mav_putvalue_instr = 0x101010B3
- Expected Output: expected_mav_putvalue = 0x0
- Observed Output in the DUT dut.mav_putvalue=0xa

Output mismatches for the above inputs proving that there is a design bug

![image](https://user-images.githubusercontent.com/84698480/182201333-822d6ece-ee32-431e-9ccd-966b4f179213.png)


## Verification Strategy


## Is the verification complete ?

