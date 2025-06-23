# Simple ALU Specification

## 1. Overview

This document specifies a simple Arithmetic Logic Unit (ALU) to be implemented in Verilog for educational and demonstration purposes. The ALU supports basic arithmetic and logical operations on two 8-bit unsigned operands.

---

## 2. Functional Description

The ALU accepts two 8-bit inputs, `A` and `B`, and performs one of four operations, selected via a 2-bit control signal `OP_SEL`. The result is output as an 8-bit signal `Y`. An overflow flag is provided for addition and subtraction.

---

## 3. Port List

| Name    | Width | Direction | Description                                 |
|---------|-------|-----------|---------------------------------------------|
| A       |   8   |   Input   | Operand A                                   |
| B       |   8   |   Input   | Operand B                                   |
| OP_SEL  |   2   |   Input   | Operation select (see Table 1)              |
| Y       |   8   |   Output  | Result                                      |
| OVF     |   1   |   Output  | Overflow flag (for ADD/SUB, else 0)         |

---

## 4. Operation Table

| OP_SEL | Operation   | Y Output        | OVF Logic                             |
|--------|-------------|-----------------|---------------------------------------|
| 00     | ADD         | A + B           | 1 if addition overflows 8 bits, else 0|
| 01     | SUB         | A - B           | 1 if subtraction underflows, else 0   |
| 10     | AND         | A & B           | 0                                     |
| 11     | OR          | A \| B          | 0                                     |

---

## 5. Timing

- All operations are combinational; no clock or reset.
- Input changes must propagate to output within one combinational delay.

---

## 6. Special Cases

- Overflow (OVF) is only meaningful for ADD and SUB.
- For logical operations (AND, OR), OVF is always 0.

---

## 7. Example Waveform

| A (hex) | B (hex) | OP_SEL | Y (hex) | OVF |
|---------|---------|--------|---------|-----|
|   7F    |   01    |  00    |   80    |  0  |
|   FF    |   01    |  00    |   00    |  1  |
|   04    |   08    |  01    |   FC    |  1  |
|   10    |   10    |  10    |   10    |  0  |
|   0F    |   F0    |  11    |   FF    |  0  |

---

## 8. Deliverables

- RTL source: `rtl/alu.v`
- Testbench: `sim/alu_tb.v`
- Specification: `spec/alu_spec.md`
- (Optional) Formal properties: `formal/alu_props.sv`

---

## 9. References

- [Wikipedia: Arithmetic Logic Unit](https://en.wikipedia.org/wiki/Arithmetic_logic_unit)
