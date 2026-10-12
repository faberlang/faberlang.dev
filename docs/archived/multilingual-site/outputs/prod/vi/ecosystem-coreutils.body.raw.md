Faber tái triển khai GNU coreutils như một minh chứng cho làn ứng dụng. Đây là các chương trình CLI thực tế, cho thấy Faber có thể xây dựng các tệp nhị phân hoạt động với argv, stdio, mã thoát và I/O của máy chủ. Kết quả được kiểm chứng bằng các tiện ích GNU trên máy chủ thông qua một bộ kiểm tra tương đương.

## Các tiện ích đã triển khai {#implemented-utilities}

**Giai đoạn 1 — khung ban đầu + true/false**  
`true`, `false`

**Giai đoạn 2 — các trình trợ giúp dùng chung + kiểm thử nội tuyến**  
`echo`, `basename`, `dirname`, `printf`, `seq`

**Giai đoạn 3 — các lát stdin nullable**  
`cat`, `head`, `tail`, `wc`, `tac`, `uniq`, `fold`, `nl`, `expand`,  
`unexpand`, `sort`, `cut`, `grep`, `tr`, `tee`, `paste`

**Đã tạo khung — Giai đoạn 5+**  
`rm`, `cp`, `mv`, `mkdir`, `touch`, `pwd`, `readlink`, `realpath`,  
`join`, `comm`, `od`, `cksum`, `split`, `yes`, `printenv`

## Ví dụ — echo {#example--echo}

Gói `echo` minh họa các mẫu Faber được sử dụng xuyên suốt coreutils:
chú thích CLI, phân tích tùy chọn, kiểm thử nội tuyến với
`probandum`/`proba`/`adfirma`, và các mô-đun dùng chung:

<<<FENCE 0>>>

## Chạy chương trình {#running}

<<<FENCE 1>>>
