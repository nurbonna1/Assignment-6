load AddSub.vm,
output-file AddSub00.out,
compare-to AddSub00.cmp,
output-list sp%D1.6.1 local%D1.6.1 argument%D1.8.1 this%D1.6.1 that%D1.6.1
            RAM[16]%D1.6.1 RAM[17]%D1.6.1 RAM[18]%D1.6.1
            local[0]%D1.8.1 local[1]%D1.8.1 local[2]%D1.8.1
            argument[0]%D1.11.1 argument[1]%D1.11.1 argument[2]%D1.11.1;

set local 0 5     // a = 5
set local 1 3     // b = 3
set static 0 4    // x = 4
run
output static 0   // Expected output: 4
