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

The assert statement is used for comparing the mux's outut to the expected value.

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
