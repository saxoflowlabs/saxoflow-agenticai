// Testbench for rtl/alu.v
module alu_testbench;

  // DUT instantiation
  alu alu_inst (
    .A(input_A),
    .B(input_B),
    .OP_SEL(operation_select),
    .Y(output_Y),
    .OVF(overflow_flag)
  );

  // Interface
  input  logic [7:0] input_A;
  input  logic [7:0] input_B;
  input  logic [1:0] operation_select;
  output logic [7:0] output_Y;
  output logic overflow_flag;

  // Internal signals
  logic [7:0] expected_output;
  logic overflow_assertion;

  // Clock generation
  logic clk = 0;
  always #5 clk = ~clk;

  // Reset generation
  logic reset = 1;
  always @(posedge clk) reset <= 0;

  // Stimulus
  initial begin
    // Reset the DUT
    @(posedge clk) reset = 1;
    @(posedge clk) reset = 0;

    // Test cases
    input_A = 8'h00;
    input_B = 8'h00;
    operation_select = 2'b00; // ADD
    #10

    input_A = 8'h01;
    input_B = 8'h01;
    operation_select = 2'b01; // SUB
    #10

    input_A = 8'hFF;
    input_B = 8'h01;
    operation_select = 2'b10; // AND
    #10

    input_A = 8'hFF;
    input_B = 8'h01;
    operation_select = 2'b11; // OR
    #10

    // Add more test cases here

    // End-of-simulation
    $finish;
  end

  // Assertions
  always_comb begin
    case (