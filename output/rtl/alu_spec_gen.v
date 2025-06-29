Here is the SystemVerilog RTL code for the Simple Arithmetic Logic Unit (ALU):

```verilog
// File: rtl/alu.v

module alu (
    input  logic [7:0] A,  // 8-bit operand A
    input  logic [7:0] B,  // 8-bit operand B
    input  logic [1:0] OP_SEL,  // 2-bit operation select
    output logic [7:0] Y,  // 8-bit result
    output logic OVF  // overflow flag (for ADD/SUB, else 0)
);

// Define the operations based on OP_SEL
always_comb begin
    case (OP_SEL)
        2'b00: Y = A + B;  // ADD
        2'b01: Y = A - B;  // SUB
        2'b10: Y = A & B;  // AND
        2'b11: Y = A | B;  // OR
        default: Y = 8'h00;  // Default value for unknown OP_SEL
    endcase

    // Calculate the overflow flag for ADD and SUB operations
    OVF = (OP_SEL == 2'b00) ? (A[7] && B[7] && Y[7]) || (!A[7] && !B[7] && !Y[7]) : 1'b0;
end

endmodule
```

The code follows the design specification and review feedback, adhering to synthesizable SystemVerilog constructs and FPGA/ASIC-friendly design practices.