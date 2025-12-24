# 🎨 東北冰雪奇緣 - 設計風格規範 (Design System)

> **用途說明**：當你需要 AI 產生類似風格的頁面時，請將此文件提供給 AI 作為參考。

---

## 📌 設計風格概述

| 項目 | 說明 |
|------|------|
| **風格名稱** | 冰雪玻璃擬態 (Frost Glassmorphism) |
| **主題** | 深色背景 + 玻璃質感卡片 + 冰雪動態效果 |
| **適用場景** | 旅遊行程、活動展示、個人專案展示 |
| **響應式** | Mobile-First，支援手機、平板、桌機 |

---

## 🎨 色彩系統 (Color Palette)

```css
:root {
    /* 主色調 */
    --ice-blue: #87CEEB;        /* 冰藍色 - 標題、強調文字 */
    --snow-white: #FFFAFA;      /* 雪白色 - 主要文字 */
    --warm-orange: #FF8C42;     /* 暖橘色 - 按鈕、互動元素、重點標示 */
    
    /* 背景色 */
    --deep-navy: #1A1A2E;       /* 深藍夜空 - 主背景 */
    --navy-mid: #16213E;        /* 中間藍 - 漸層用 */
    --navy-light: #0F3460;      /* 淺藍 - 漸層用 */
    --frost-blue: #E8F4F8;      /* 霜藍 - 淺色區塊背景 */
    
    /* 玻璃效果 */
    --glass-bg: rgba(255,255,255,0.1);      /* 玻璃背景 */
    --glass-border: rgba(255,255,255,0.2);  /* 玻璃邊框 */
    
    /* 功能色 */
    --success-green: #4CAF50;   /* 成功/完成 */
    --danger-red: #f44336;      /* 警告/刪除 */
}
```

### 背景漸層
```css
background: linear-gradient(135deg, var(--deep-navy) 0%, #16213E 50%, #0F3460 100%);
```

---

## 📝 字型系統 (Typography)

```css
font-family: 'Microsoft JhengHei', 'Noto Sans TC', sans-serif;
```

| 元素 | 字級 | 顏色 | 備註 |
|------|------|------|------|
| 主標題 H1 | 2.8em | snow-white | 帶陰影 `text-shadow: 2px 2px 8px rgba(0,0,0,0.5)` |
| 區塊標題 | 1.8em | ice-blue | 置中，帶圖示 |
| 卡片標題 | 1.2em | snow-white | - |
| 內文 | 1em (16px) | snow-white | opacity: 0.9 |
| 小字/標籤 | 0.75em~0.9em | snow-white | opacity: 0.7~0.8 |

---

## 🧊 玻璃擬態卡片 (Glassmorphism Card)

```css
.glass-card {
    background: var(--glass-bg);           /* 半透明白 */
    backdrop-filter: blur(10px);           /* 模糊效果 */
    -webkit-backdrop-filter: blur(10px);   /* Safari 支援 */
    border: 1px solid var(--glass-border); /* 微透邊框 */
    border-radius: 15px~20px;              /* 圓角 */
    padding: 20px~25px;
    transition: all 0.3s ease;
}

/* 懸停效果 */
.glass-card:hover {
    transform: translateY(-3px);
    background: rgba(255,255,255,0.15);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
```

---

## 🔘 按鈕樣式 (Buttons)

### 主要按鈕 (Primary)
```css
.btn-primary {
    background: var(--warm-orange);
    color: white;
    border: none;
    border-radius: 25px;          /* 膠囊形狀 */
    padding: 12px 30px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-primary:hover {
    background: #FF7A30;
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(255,140,66,0.4);
}
```

### 次要按鈕 (Secondary/Glass)
```css
.btn-secondary {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    color: var(--snow-white);
    border-radius: 12px;
    padding: 8px 16px;
}
```

---

## 📱 底部導航 (Mobile Bottom Navigation)

```css
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(26, 26, 46, 0.95);
    backdrop-filter: blur(20px);
    display: flex;
    justify-content: space-around;
    padding: 10px 5px;
    z-index: 999;
    border-top: 1px solid var(--glass-border);
}

.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 8px 12px;
    color: var(--snow-white);
    opacity: 0.6;
    transition: all 0.3s;
    border-radius: 10px;
    font-size: 0.75em;
}

.nav-item.active {
    opacity: 1;
    background: var(--glass-bg);
}

.nav-item.active i {
    color: var(--warm-orange);  /* 選中狀態用暖橘色 */
}
```

---

## ❄️ 飄雪動畫 (Snow Animation)

```css
.snowflakes {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1000;
    overflow: hidden;
}

.snowflake {
    position: absolute;
    color: #fff;
    opacity: 0.8;
    animation: fall linear infinite;
}

@keyframes fall {
    0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
    100% { transform: translateY(110vh) rotate(360deg); opacity: 0.3; }
}
```

### JavaScript 生成雪花
```javascript
function createSnowflakes() {
    const container = document.querySelector('.snowflakes');
    const flakes = ['❄', '❅', '❆', '✻', '✼', '❉'];
    
    for (let i = 0; i < 50; i++) {
        const flake = document.createElement('div');
        flake.className = 'snowflake';
        flake.innerHTML = flakes[Math.floor(Math.random() * flakes.length)];
        flake.style.left = Math.random() * 100 + '%';
        flake.style.fontSize = (Math.random() * 15 + 8) + 'px';
        flake.style.animationDuration = (Math.random() * 5 + 5) + 's';
        flake.style.animationDelay = Math.random() * 10 + 's';
        container.appendChild(flake);
    }
}
```

---

## ✨ 動畫效果 (Animations)

### 淡入動畫
```css
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.animated-element {
    animation: fadeIn 0.4s ease;
}
```

### 通用過渡
```css
transition: all 0.3s ease;
```

---

## 🏷️ 標籤/徽章 (Badge/Tag)

```css
.badge {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 10px 20px;
    backdrop-filter: blur(10px);
}

.badge i {
    color: var(--warm-orange);
    margin-right: 5px;
}
```

---

## 📐 間距規範 (Spacing)

| 用途 | 大小 |
|------|------|
| 區塊內距 (padding) | 20px ~ 40px |
| 元素間距 (gap) | 10px ~ 20px |
| 卡片內距 | 15px ~ 25px |
| 圓角 (border-radius) | 10px ~ 20px |
| 底部導航高度 | ~70px |

---

## 🖼️ 圖示庫 (Icons)

使用 **Font Awesome 6**：
```html
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
```

常用圖示：
- 首頁：`fa-home`
- 行程：`fa-calendar-days`
- 地圖：`fa-map-location-dot`
- 清單：`fa-list-check`
- 設定：`fa-gear`
- 雪花：`fa-snowflake`
- 溫度：`fa-temperature-low`
- 餐廳：`fa-utensils`
- 飯店：`fa-bed`
- 景點：`fa-mountain-sun`

---

## 📱 響應式斷點 (Breakpoints)

```css
/* 手機優先 */
@media (min-width: 768px) {
    /* 平板 */
}

@media (min-width: 1024px) {
    /* 桌機 */
}
```

---

## 🔧 HTML 基本結構範本

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>頁面標題 - 東北冰雪奇緣</title>
    <meta name="theme-color" content="#1A1A2E">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        /* 載入 CSS 變數與基本樣式 */
    </style>
</head>
<body>
    <!-- 飄雪效果 -->
    <div class="snowflakes"></div>
    
    <!-- 主要內容 -->
    <main class="section">
        <h2 class="section-title"><i class="fas fa-icon"></i> 區塊標題</h2>
        <!-- 內容 -->
    </main>
    
    <!-- 底部導航 -->
    <nav class="bottom-nav">
        <a href="index.html" class="nav-item">
            <i class="fas fa-home"></i>
            <span>首頁</span>
        </a>
        <!-- 更多導航項目 -->
    </nav>
    
    <script>
        // 雪花動畫
        createSnowflakes();
    </script>
</body>
</html>
```

---

## 💡 設計原則

1. **深色主題**：使用深藍色系背景，營造夜空感
2. **玻璃質感**：卡片使用半透明白 + blur 效果
3. **暖色點綴**：橘色用於重點元素，與冷色調形成對比
4. **動態細節**：飄雪動畫增添氛圍，hover 效果增加互動感
5. **手機優先**：底部導航、大觸控區域、適當的字級

---

## 📋 使用方式

當你需要 AI 產生新頁面時，請在對話中說明：

> 請參考 `STYLE_GUIDE.md` 的設計規範，幫我建立一個 [頁面描述]，
> 風格要保持「冰雪玻璃擬態」主題，使用相同的色彩系統和元件樣式。

或直接將此文件內容貼給 AI 參考。
