#!/usr/bin/env python3
"""批量更新风格页面，使用共享导航/页脚组件"""

import re
import os

STYLES = {
    '01': ('minimalism', '极简主义', 'Minimalism'),
    '02': ('neumorphism', '新拟态', 'Neumorphism'),
    '03': ('glassmorphism', '玻璃态', 'Glassmorphism'),
    '04': ('brutalism', '野兽派', 'Brutalism'),
    '05': ('flat-design', '扁平设计', 'Flat Design'),
    '06': ('cyberpunk', '赛博朋克', 'Cyberpunk'),
    '07': ('vaporwave', '蒸汽波', 'Vaporwave'),
    '08': ('swiss-modernism', '瑞士现代主义', 'Swiss Modernism'),
    '09': ('memphis', '孟菲斯', 'Memphis'),
    '10': ('claymorphism', '粘土态', 'Claymorphism'),
    '11': ('dark-mode', '暗黑模式', 'Dark Mode'),
    '12': ('retro-futurism', '复古未来主义', 'Retro-Futurism'),
    '13': ('e-ink', '电子墨水', 'E-Ink'),
    '14': ('aurora-ui', '极光 UI', 'Aurora UI'),
    '15': ('liquid-glass', '液体玻璃', 'Liquid Glass'),
    '16': ('hud-scifi', 'HUD 科幻', 'HUD Sci-Fi'),
    '17': ('pixel-art', '像素艺术', 'Pixel Art'),
    '18': ('skeuomorphism', '拟物主义', 'Skeuomorphism'),
    '19': ('motion-driven', '动态驱动', 'Motion-Driven'),
    '20': ('bento-grid', 'Bento 网格', 'Bento Grid'),
    '21': ('zero-ui', '零界面', 'Zero UI'),
    '22': ('hero-centric', '英雄中心', 'Hero-Centric'),
    '23': ('organic-biomimicry', '有机仿生', 'Organic Biomimicry'),
    '24': ('soft-ui', '软 UI', 'Soft UI'),
    '25': ('gen-z-chaos', 'Z世代混乱', 'Gen-Z Chaos'),
    '26': ('neubrutalism', '新粗野主义', 'Neubrutalism'),
    '27': ('ai-native', 'AI 原生', 'AI-Native'),
    '28': ('inclusive-design', '包容性设计', 'Inclusive Design'),
    '29': ('spatial-ui', '空间 UI', 'Spatial UI'),
    '30': ('y2k', 'Y2K 复兴', 'Y2K Revival'),
    '31': ('ancient-spellbook', '古老魔法书', 'Ancient Spellbook'),
}

# 前后风格映射
NUM_ORDER = ['01','02','03','04','05','06','07','08','09','10',
             '11','12','13','14','15','16','17','18','19','20',
             '21','22','23','24','25','26','27','28','29','30','31']

def get_prev_next(num):
    idx = NUM_ORDER.index(num)
    prev_num = NUM_ORDER[idx - 1] if idx > 0 else None
    next_num = NUM_ORDER[idx + 1] if idx < len(NUM_ORDER) - 1 else None
    return prev_num, next_num

def make_nav_placeholder(num, lang, base_path):
    """生成共享导航占位符"""
    name = STYLES[num][1] if lang == 'zh' else STYLES[num][2]
    name_en = STYLES[num][2]
    return (
        f'<div id="shared-nav" data-style="{num}" data-name="{name}" '
        f'data-name-en="{name_en}" data-lang="{lang}" data-base="{base_path}"></div>'
    )

def make_footer_placeholder(num, lang):
    """生成共享页脚占位符"""
    prev_num, next_num = get_prev_next(num)
    prev_name = STYLES[prev_num][1] if prev_num and lang == 'zh' else (STYLES[prev_num][2] if prev_num else '')
    next_name = STYLES[next_num][1] if next_num and lang == 'zh' else (STYLES[next_num][2] if next_num else '')
    attrs = f' data-style="{num}"'
    if prev_num:
        attrs += f' data-prev="{prev_num}" data-prev-name="{prev_name}"'
    if next_num:
        attrs += f' data-next="{next_num}" data-next-name="{next_name}"'
    return f'<div id="shared-footer"{attrs}></div>'

def update_file(filepath, num, lang, base_path):
    """更新单个文件"""
    if not os.path.exists(filepath):
        print(f'  SKIP (not found): {filepath}')
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 替换导航: <nav ...> ... </nav>
    # 处理各种 nav 变体，包括带 style 属性的
    nav_pattern = re.compile(r'<!--\s*Navigation\s*-->\s*<nav\b[^>]*>.*?</nav>', re.DOTALL)
    # 也匹配没有注释的导航
    nav_pattern2 = re.compile(r'<nav\b[^>]*>.*?</nav>', re.DOTALL)

    nav_placeholder = make_nav_placeholder(num, lang, base_path)

    if nav_pattern.search(content):
        content = nav_pattern.sub(nav_placeholder, content, count=1)
    elif nav_pattern2.search(content):
        content = nav_pattern2.sub(nav_placeholder, content, count=1)

    # 替换页脚: <footer ...> ... </footer>
    footer_pattern = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL)
    footer_placeholder = make_footer_placeholder(num, lang)

    if footer_pattern.search(content):
        content = footer_pattern.sub(footer_placeholder, content, count=1)

    # 添加 shared/components.js 脚本（在 </body> 之前，且不重复）
    script_tag = f'<script src="{base_path}shared/components.js"></script>'
    if script_tag not in content:
        content = content.replace('</body>', f'  {script_tag}\n</body>')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  UPDATED: {filepath}')
    else:
        print(f'  UNCHANGED: {filepath}')

def main():
    # 中文版 (styles/)
    for num, (filename, name_zh, name_en) in STYLES.items():
        # 跳过 ancient-spellbook（它有完全自定义的导航）
        if num == '31':
            print(f'  SKIP #31 (custom nav): styles/{filename}.html')
            continue
        filepath = f'styles/{filename}.html'
        update_file(filepath, num, 'zh', '../')

    # 英文版 (zh/styles/)
    for num, (filename, name_zh, name_en) in STYLES.items():
        if num == '31':
            print(f'  SKIP #31 (custom nav): zh/styles/{filename}.html')
            continue
        filepath = f'zh/styles/{filename}.html'
        update_file(filepath, num, 'en', '../../')

    print('\nDone!')

if __name__ == '__main__':
    main()