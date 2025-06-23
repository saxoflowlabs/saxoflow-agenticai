```systemverilog
// Check if OVF remains low after reset
assert property (@(posedge clk) disable iff (!rst_n) rst_n |-> always(!OVF)) else $error("OVF not reset correctly");

// Check input stability
assert property (@(posedge clk) disable iff (!rst_n) $stable(A)) else $error("A is not stable");
assert property (@(posedge clk) disable iff (!rst_n) $stable(B)) else $error("B is not stable");
assert property (@(posedge clk) disable iff (!rst_n) $stable(OP_SEL)) else $error("OP_SEL is not stable");

// Check OP_SEL range
assert property (@(posedge clk) disable iff (!rst_n) (OP_SEL inside {[2'b00:2'b11]})) else $error("OP_SEL out of range");

// Check OVF behavior for addition and subtraction
assert property (@(posedge clk) disable iff (!rst_n) (OP_SEL == 2'b00 && A == 8'h7F && B == 8'h01) |-> OVF) else $error("OVF not set for addition overflow");
assert property (@(posedge clk) disable iff (!rst_n) (OP_SEL == 2'b00 && A == 8'h80 && B == 8'hFF) |-> OVF) else $error("OVF not set for addition underflow");
assert property (@(posedge clk) disable iff (!rst_n) (OP_SEL == 2'b01 && A == 8'h80 && B == 8'h01) |-> OVF) else $error("OVF not set for subtraction underflow");
assert property (@(posedge clk) disable iff (!rst_n) (OP_SEL == 2'b01 && A == 8'h7F && B == 8'hFF) |-> OVF) else $error("OVF not set for subtraction overflow");

// Check relationship between Y and OVF for addition and subtraction
assert property (@(posedge clk) disable iff (!rst_n) (OP_SEL == 2'b00 && OVF) |-> (Y == 8'h7F || Y == 8'h80)) else $error("Y not saturated for addition overflow");
assert property (@(posedge clk) disable iff (!rst_n) (OP_SEL == 2'b01 && OVF) |-> (Y == 8'h7F || Y