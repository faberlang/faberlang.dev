## Rẽ nhánh điều kiện {#conditional-branching}

### si / sin / secus {#si-sin-secus}

<<<FENCE 0>>>

Với `else-if` và `else`:

<<<FENCE 1>>>

### Nhánh rút gọn với ∴ {#compact-branch-with}

Thân nhánh chỉ gồm một câu lệnh sử dụng `∴` (hoặc bí danh `ergo`):

<<<FENCE 2>>>

## Lặp {#iteration}

### Giá trị — itera ex {#values-itera-ex}

<<<FENCE 3>>>

### Khóa — itera de {#keys-itera-de}

<<<FENCE 4>>>

### Khoảng — itera ab {#range-itera-ab}

<<<FENCE 5>>>

## Vòng lặp while {#while-loops}

<<<FENCE 6>>>

## Khối bảo vệ — custodi {#guard-sections-custodi}

`custodi` nhóm các kiểm tra thoát sớm trước thân chính của một hàm.
Mỗi mệnh đề `si` là một điều kiện bảo vệ được kiểm tra tuần tự:

<<<FENCE 7>>>

Trong v1, không thể dùng `break` trong `custodi` — đây là lan can bảo vệ, không phải vòng lặp.

## Đối sánh mẫu — elige {#pattern-matching-elige}

`elige` chọn nhánh khớp đầu tiên:

<<<FENCE 8>>>

## Đối sánh union có thẻ — discerne {#tagged-union-matching-discerne}

`discerne` đối sánh đầy đủ các biến thể của `discretio`:

<<<FENCE 9>>>

## Khối try — fac / cape {#try-blocks-fac-cape}

`fac` mở một khối có thể phát sinh lỗi, còn `cape` khôi phục khi lỗi xảy ra:

<<<FENCE 10>>>
