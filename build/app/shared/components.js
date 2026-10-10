/**
 * Design Inspiration Gallery — Shared UI Components
 * 自动检测页面上下文，渲染导航栏和页脚
 */
(function () {
  var nav = document.getElementById('shared-nav');
  var footer = document.getElementById('shared-footer');
  if (!nav && !footer) return;

  // 从 data 属性读取页面信息
  var styleNum = nav ? nav.getAttribute('data-style') : '';
  var styleName = nav ? nav.getAttribute('data-name') : '';
  var styleNameEn = nav ? nav.getAttribute('data-name-en') : '';
  var lang = nav ? nav.getAttribute('data-lang') : 'zh';
  var basePath = nav ? nav.getAttribute('data-base') : '../';

  var isZh = lang === 'zh';
  var backLabel = isZh ? '返回画廊' : 'Back to Gallery';
  var styleLabel = isZh ? '设计风格' : 'Style';
  var langLabel = isZh ? '中文' : '中文';
  var enLabel = 'EN';

  // 语言对应的画廊首页：中文版在根目录，英文版在 zh/ 目录
  var galleryPath = isZh ? basePath + 'index.html' : basePath + 'zh/index.html';

  // ── 导航栏 ──
  if (nav) {
    nav.outerHTML =
      '<nav class="fixed top-4 left-4 right-4 bg-white/95 backdrop-blur-sm border border-gray-200 rounded-xl z-50 shadow-sm" style="max-width:calc(100% - 32px)">' +
      '<div class="max-w-7xl mx-auto px-5 py-3 flex justify-between items-center">' +
      '<a href="' + galleryPath + '" class="text-sm text-gray-500 hover:text-black transition-colors">&larr; ' +
      backLabel +
      '</a>' +
      '<span class="font-medium text-sm text-gray-700">#' +
      styleNum +
      ' ' +
      '<span class="' + (isZh ? '' : 'hidden') + '">' +
      styleName +
      '</span>' +
      '<span class="' + (isZh ? 'hidden' : '') + '">' +
      styleNameEn +
      '</span>' +
      '</span>' +
      '<div class="flex items-center gap-2 text-xs">' +
      (isZh
        ? '<a href="' + basePath + 'zh/styles/' + getStyleFile(styleNum) + '.html" class="text-gray-400 hover:text-gray-600">' + enLabel + '</a>' +
          '<span class="text-gray-300">|</span>' +
          '<span class="text-gray-800 font-medium">' + langLabel + '</span>'
        : '<span class="text-gray-800 font-medium">' + enLabel + '</span>' +
          '<span class="text-gray-300">|</span>' +
          '<a href="' + basePath + 'styles/' + getStyleFile(styleNum) + '.html" class="text-gray-400 hover:text-gray-600">' + langLabel + '</a>') +
      '</div>' +
      '</div>' +
      '</nav>';
  }

  // ── 页脚 ──
  if (footer) {
    var prev = footer.getAttribute('data-prev');
    var next = footer.getAttribute('data-next');
    var prevName = footer.getAttribute('data-prev-name') || '';
    var nextName = footer.getAttribute('data-next-name') || '';
    var prevPath = prev ? getStyleFile(prev) : '';
    var nextPath = next ? getStyleFile(next) : '';

    var prevHtml = prev
      ? '<a href="' + prevPath + '.html" class="text-sm text-gray-500 hover:text-black transition-colors">&larr; ' + prevName + '</a>'
      : '<span></span>';
    var nextHtml = next
      ? '<a href="' + nextPath + '.html" class="text-sm text-gray-500 hover:text-black transition-colors">' + nextName + ' &rarr;</a>'
      : '<span></span>';

    footer.outerHTML =
      '<footer class="border-t border-gray-100 py-8 px-6 mt-12">' +
      '<div class="max-w-7xl mx-auto flex justify-between items-center">' +
      prevHtml +
      '<a href="' + galleryPath + '" class="text-sm text-gray-400 hover:text-gray-600">' +
      (isZh ? '返回画廊' : 'Back to Gallery') +
      '</a>' +
      nextHtml +
      '</div>' +
      '</footer>';
  }

  // 将风格编号映射为文件名
  function getStyleFile(num) {
    var map = {
      '01': 'minimalism', '02': 'neumorphism', '03': 'glassmorphism',
      '04': 'brutalism', '05': 'flat-design', '06': 'cyberpunk',
      '07': 'vaporwave', '08': 'swiss-modernism', '09': 'memphis',
      '10': 'claymorphism', '11': 'dark-mode', '12': 'retro-futurism',
      '13': 'e-ink', '14': 'aurora-ui', '15': 'liquid-glass',
      '16': 'hud-scifi', '17': 'pixel-art', '18': 'skeuomorphism',
      '19': 'motion-driven', '20': 'bento-grid', '21': 'zero-ui',
      '22': 'hero-centric', '23': 'organic-biomimicry', '24': 'soft-ui',
      '25': 'gen-z-chaos', '26': 'neubrutalism', '27': 'ai-native',
      '28': 'inclusive-design', '29': 'spatial-ui', '30': 'y2k',
      '31': 'ancient-spellbook'
    };
    return map[num] || 'minimalism';
  }
})();