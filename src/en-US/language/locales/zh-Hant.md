+++
title = "Traditional Chinese reader locale"
section = "locales"
order = 17
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

**繁體中文** — the `zh-Hant` reader pack. Script: Han (Traditional); direction: left-to-right.

| Field | Value |
|---|---|
| **Locale code** | `zh-Hant` |
| **Native name** | 繁體中文 |
| **Script** | Han (Traditional) |
| **Direction** | left-to-right |

A sibling pack, not a variant spelling: it carries different vocabulary (定值 against 常量) over the same semantics.

## English ↔ Traditional Chinese {#mapping}

Generated from the packs; the canonical (Latin) name keys the full [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          繁體中文
| ---------------  --------------
| all              全部
| and              且
| any              任一
| argmax           最大值索引
| argmin           最小值索引
| args             引數
| as               作為
| assert           斷言
| async            異步
| async_generator  異流
| async_main       非同步入口
| async_setup      準備非同步
| async_teardown   後置準備非同步
| at               在
| await            等棄
| await_const      等定
| await_var        等變
| before           之前
| bench            測量
| between          之間
| break            中斷
| call             端點
| case             分支
| catch            捕捉
| class            類型
| cli              命令行
| coalesce         或取
| column           欄位
| command          命令
| comptime         前綴
| const            定值
| continue         繼續
| conversion       轉換
| —                變換
| copy             拷貝
| count            計數
| cursor           迭代器
| debug            檢視
| default          預設
| describe         測試規格
| description      描述
| do               執行
| elif             否則若
| else             否則
| embed            嵌入
| empty            空集
| enum             列舉
| errors           錯誤
| exit             出口
| expect_failure   預期失敗
| false            假
| flaky            脆弱
| fn               函式
| for              遍歷
| format           格式文字
| fragment         片段
| free             自由
| from             取自
| future           未來
| generator        流
| global           全局
| guard            守衛
| if               若
| implements       實作
| import           匯入
| interface        待實作介面
| internal         內部
| is               是
| kernel           內核
| lambda           閉包
| lane             車道
| let              設為
| line             行
| long             詳
| main             入口
| match            比對
| max              最大
| min              最小
| module           模組
| mut              傳入
| name             名稱
| nan              nan
| nihil            空
| not              非
| null             可空
| only             僅限
| only_in          僅限於
| operand          操作數
| option           選項
| optional         可選
| options          可選項
| or               或
| own              擁有
| panic            崩潰
| pass             靜默
| per              按
| primus_quem      primus_quem
| print            註記
| private          私有
| product          求積
| protected        保護
| public           公開
| radix            radix
| range            範圍
| read             讀取
| readonly         不變
| reduce           歸約
| ref              從
| reject           拒絕
| rename           改名
| repeat           重複
| require          需要
| rest             其餘
| return           傳回
| return_await     等返
| schema           結構
| self             自身
| setup            準備
| shared           commune
| short            簡
| size             尺寸
| skip             略過
| spread           展開
| static           靜態
| step             每
| sum              求和
| switch           選擇
| tag              標籤
| teardown         後置準備
| test             測試
| then             則
| thread           執行緒
| throw            拋出
| throws           可拋
| timeout          時限
| todo             預期
| trap             陷阱
| true             真
| tuple            元組
| type             型別
| ubi              ubi
| union            分支聯集
| unstable         不穩定
| until            直到
| var              變值
| variant          虛構
| vertex           頂點
| via              經由
| warn             警告
| while            當
| within           內含
| wrapping         模數
| write            寫出
| yield            讓出
```

### Types {#types}

```text locale=la
| English      繁體中文
| -----------  ----------
| any          任意值
| ascii        ascii
| atomic       原子
| bool         布林
| byte         單位元組
| bytes        位元組
| census       普查
| channel      通道
| char         字元
| filter       篩選器
| float        小數
| frame        幀
| instant      執行個體
| int          整數
| intervallum  區間
| iterator     游標
| json         JSON
| list         列表
| map          表格
| matrix       矩陣
| never        永不
| none         無
| object       物件
| promise      承諾
| queue        佇列
| record       ratio
| recv         接收
| regex        正規表示式
| saturating   飽和
| send         發送
| series       序列
| set          副本
| sparsa       稀疏
| stack        堆疊
| string       文字
| tensor       張量
| trapping     精確
| unknown      未知
| value        值
| vector       向量
| void         空值
| wrapping_ty  模數类型
```

### Intrinsics {#intrinsics}

```text locale=la
| English               繁體中文
| --------------------  ----------
| abs                   絕對值
| add                   新增
| added                 已新增
| added_bias            加偏置
| all                   全部
| any                   任一
| append                附加
| apply                 套用
| approx                近似
| argmax                最大值索引
| argmin                最小值索引
| at_least              至少
| at_most               至多
| bit_and               位元與
| bit_and_assign        位元與指派
| bit_or                位元或
| bit_or_assign         位元或指派
| ceiling               向上取整
| clamp                 限幅
| compare_exchange      比較並交換
| complement            取補
| complemented          已取補
| contains              包含
| cos                   餘弦
| create                建立
| cross                 叉積
| cross_entropy         交叉熵
| cumulate              累積
| cursor                游標
| delete                刪除
| densify               稠密化
| difference            差集
| divide                除以
| divide                除法
| divided               已除以
| dot                   點積
| drop                  捨棄
| end                   結束
| ends_with             結尾是
| escape                跳脫
| exchange              交換
| exp                   指數
| fill                  填充
| filter                過濾
| find                  尋找
| find_all              尋找全部
| first                 第一個
| flatten               展平
| flip                  翻轉
| flipped               已翻轉
| floor                 向下取整
| formata               formata
| from_flat             由扁平建構
| gather                收集
| gelu                  gelu
| get                   取得
| greater               大於
| group                 分組
| has                   含有
| intersect             相交
| intersection          交集
| invert                求逆
| is_empty              為空
| is_subset             是子集
| is_superset           是超集
| keys                  鍵列表
| last                  最後一個
| layer_norm            層正規化
| length                長度
| less                  小於
| ln                    自然對數
| load                  載入
| log10                 常用對數
| lowercase             小寫
| map                   變換
| matches               比對
| materialize           物化
| matmul                矩陣乘法
| maximum               最大值
| mean                  平均值
| minimum               最小值
| modulo                取餘
| modulo_assign         取餘指派
| multiplied            已乘以
| multiply              乘以
| named                 命名分組
| negate                取負
| negated               已取負
| nonzero_count         非零個數
| normalize             正規化
| power                 乘冪
| put                   放入
| reduce                歸約
| relu                  ReLU
| remove_first          移除首項
| remove_last           移除末項
| replace               替換
| reshape               重塑
| reverse               反轉
| rms_norm              rms_norm
| rope_norm             rope_norm
| round                 四捨五入
| set                   設定
| shape                 形狀
| shift_left            左移
| shift_right           右移
| shifted_left          已左移
| shifted_right         已右移
| sign                  符號
| silu                  silu
| sin                   正弦
| slice                 切片
| softmax               Softmax
| sort                  排序
| sorted                已排序
| split                 分割
| sqrt                  平方根
| start                 起始
| starts_with           開頭是
| store                 儲存
| subtract              減去
| subtracted            已減去
| sum                   求和
| swizzle               swizzle
| symmetric_difference  對稱差集
| take                  取前
| take_last             取後
| tan                   正切
| text                  文字
| transpose             轉置
| trim                  修剪空白
| truncate              截斷
| union                 聯集
| union                 聯集
| uppercase             大寫
| values                值列表
```

---

[All reader locales](/language/reader-locales.html) · [Full keyword mapping](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
