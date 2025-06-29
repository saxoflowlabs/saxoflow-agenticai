```systemverilog
// Check if OVF is correctly calculated for ADD operation
property p_ovf_add;
    @(posedge clk) disable iff (!rst_n)
    (OP_SEL == 2'b00) |-> (OVF == ((A[7] && B[7] && !Y[7]) || (!A[7] && !B[7] && Y[7])));
endproperty
assert property (p_ovf_add);

// Check if OVF is correctly calculated for SUB operation
property p_ovf_sub;
    @(posedge clk) disable iff (!rst_n)
    (OP_SEL == 2'b01) |-> (OVF == ((A[7] && !B[7] && !Y[7]) || (!A[7] && B[7] && Y[7])));
endproperty
assert property (p_ovf_sub);

// Check if OVF is 0 for non-ADD/SUB operations
property p_ovf_non_add_sub;
    @(posedge clk) disable iff (!rst_n)
    (OP_SEL != 2'b00 && OP_SEL != 2'b01) |-> (OVF == 0);
endproperty
assert property (p_ovf_non_add_sub);

// Check input stability
property p_input_stable;
    @(posedge clk) disable iff (!rst_n)
    $stable(A) && $stable(B) && $stable(OP_SEL);
endproperty
assert property (p_input_stable);

// Check reset behavior for Y and OVF
property p_reset_behavior_y;
    @(posedge clk) disable iff (rst_n)
    !rst_n |-> (Y == 0);
endproperty
assert property (p_reset_behavior_y);

property p_reset_behavior_ovf;
    @(posedge clk) disable iff (rst_n)
    !rst_n |-> (OVF == 0);
endproperty
assert property (p_reset_behavior_ovf);

// Check if Y is correctly calculated for each operation
property p_y_add;
    @(posedge clk) disable iff (!rst_n)
    (OP_SEL == 2'b00) |-> (Y == $past(A) + $past(B));
endproperty
assert property (p_y_add);

property p_y_sub;
    @(posedge clk) disable iff (!rst_n)
    (OP_SEL == 2'b01) |-> (Y == $past(A) - $past