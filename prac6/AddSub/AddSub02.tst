load AddSub.vm,
output-file AddSub00.out,
compare-to AddSub00.cmp,
output-list sp%D1.6.1 local%D1.6.1 argument%D1.8.1 this%D1.6.1 that%D1.6.1
            RAM[16]%D1.6.1 RAM[17]%D1.6.1 RAM[18]%D1.6.1
            local[0]%D1.8.1 local[1]%D1.8.1 local[2]%D1.8.1
            argument[0]%D1.11.1 argument[1]%D1.11.1 argument[2]%D1.11.1;

set local 0 10    // a = 10
set local 1 2     // b = 2
set static 0 5    // x = 5
run
output static 0   // Expected output: 7 (because (10 + 2) - 5 = 7)
