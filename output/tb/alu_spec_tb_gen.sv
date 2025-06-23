```systemverilog
// File: alu_testbench.sv

module alu_testbench;

    // Import DUT interface
    import alu_pkg::*;

    // Instantiate the DUT
    alu alu_inst (
        .A(alu_A),
        .B(alu_B),
        .OP_SEL(alu_OP_SEL),
        .Y(alu_Y),
        .OVF(alu_OVF)
    );

    // Clock generation
    logic clk;
    always #5 clk = ~clk;

    // Asynchronous reset
    logic async_rst;

    // DUT inputs
    alu_A = 8'b0;
    alu_B = 8'b0;
    alu_OP_SEL = 2'b00;

    // Connect reset signal
    assign async_rst = !clk;

    // Functional coverage
    covergroup alu_coverage is
        function void cover(input [7:0] a, input [7:0] b, input [1:0] op_sel);
            if (a == 8'b0) begin
                if (b == 8'b255) begin
                    if (op_sel == 2'b00) begin
                        if (alu_Y == 8'b255) coverpoint op_sel with {default: '0, '1 => '1};
                    end else if (op_sel == 2'b01) begin
                        if (alu_Y == 8'b0) coverpoint op_sel with {default: '0, '1 => '1};
                    end
                end
            end
            // Add more coverage points here
        endfunction
    endgroup

    // Create a coverage object
    alu_coverage cov_obj;

    // Testbench initialization
    initial begin
        // Initialize clock and reset
        clk = 1'b0;
        async_rst = 1'b1;

        // Wait for reset to de-assert
        @(posedge clk) async_rst