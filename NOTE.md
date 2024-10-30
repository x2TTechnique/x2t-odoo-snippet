# Visual Studio Code Snippet Variables

| **Variables**              | **Description**                                                   |
| -------------------------- | ----------------------------------------------------------------- |
| `TM_SELECTED_TEXT`         | Văn bản đang được chọn hoặc chuỗi rỗng nếu không có gì được chọn. |
| `TM_CURRENT_LINE`          | Nội dung của dòng hiện tại.                                       |
| `TM_CURRENT_WORD`          | Từ dưới con trỏ hoặc chuỗi rỗng nếu không có từ nào.              |
| `TM_LINE_INDEX`            | Số dòng theo **chỉ mục 0** (zero-indexed).                        |
| `TM_LINE_NUMBER`           | Số dòng theo **chỉ mục 1** (one-indexed).                         |
| `TM_FILENAME`              | Tên file hiện tại.                                                |
| `TM_FILENAME_BASE`         | Tên file không có phần mở rộng.                                   |
| `TM_DIRECTORY`             | Thư mục chứa file hiện tại.                                       |
| `TM_FILEPATH`              | Đường dẫn đầy đủ của file hiện tại.                               |
| `RELATIVE_FILEPATH`        | Đường dẫn tương đối đến file từ **workspace** hoặc thư mục mở.    |
| `CLIPBOARD`                | Nội dung của **clipboard** hiện tại.                              |
| `WORKSPACE_NAME`           | Tên của **workspace** hoặc thư mục đang mở.                       |
| `WORKSPACE_FOLDER`         | Đường dẫn đến **workspace** hoặc thư mục đang mở.                 |
| `CURSOR_INDEX`             | Chỉ số con trỏ dựa trên **zero-index**.                           |
| `CURSOR_NUMBER`            | Chỉ số con trỏ dựa trên **one-index**.                            |
| `CURRENT_YEAR`             | Năm hiện tại.                                                     |
| `CURRENT_YEAR_SHORT`       | Hai chữ số cuối của năm hiện tại.                                 |
| `CURRENT_MONTH`            | Tháng hiện tại (2 chữ số, ví dụ: `02`).                           |
| `CURRENT_MONTH_NAME`       | Tên tháng đầy đủ (ví dụ: `July`).                                 |
| `CURRENT_MONTH_NAME_SHORT` | Tên viết tắt của tháng (ví dụ: `Jul`).                            |
| `CURRENT_DATE`             | Ngày trong tháng (2 chữ số, ví dụ: `08`).                         |
| `CURRENT_DAY_NAME`         | Tên ngày (ví dụ: `Monday`).                                       |
| `CURRENT_DAY_NAME_SHORT`   | Tên viết tắt của ngày (ví dụ: `Mon`).                             |
| `CURRENT_HOUR`             | Giờ hiện tại theo **định dạng 24 giờ**.                           |
| `CURRENT_MINUTE`           | Phút hiện tại (2 chữ số).                                         |
| `CURRENT_SECOND`           | Giây hiện tại (2 chữ số).                                         |
| `CURRENT_SECONDS_UNIX`     | Số giây từ **Unix epoch** (1970-01-01).                           |
| `CURRENT_TIMEZONE_OFFSET`  | Chênh lệch múi giờ so với UTC (ví dụ: `-07:00`).                  |
| `RANDOM`                   | 6 chữ số ngẫu nhiên (hệ cơ số 10).                                |
| `RANDOM_HEX`               | 6 chữ số ngẫu nhiên (hệ cơ số 16).                                |
| `UUID`                     | UUID phiên bản 4 ngẫu nhiên.                                      |
| `BLOCK_COMMENT_START`      | Ký tự bắt đầu bình luận khối (ví dụ: `<!--` trong HTML).          |
| `BLOCK_COMMENT_END`        | Ký tự kết thúc bình luận khối (ví dụ: `-->`).                     |
| `LINE_COMMENT`             | Ký tự bình luận dòng đơn (phụ thuộc vào ngôn ngữ).                |
