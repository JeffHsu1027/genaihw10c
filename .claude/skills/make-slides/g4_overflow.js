// G4 溢出量測：在瀏覽器開啟 deck.html 後執行，回傳每頁是否有內容超出 16:9 版面。
// 只量測，不修改頁面。
(() => {
  const slides = [...document.querySelectorAll("section.slide")];
  const rows = slides.map((s, i) => {
    const over = s.scrollHeight > s.clientHeight + 1 || s.scrollWidth > s.clientWidth + 1;
    return { slide: i + 1, id: s.id, overflow: over, scrollHeight: s.scrollHeight, clientHeight: s.clientHeight };
  });
  return { slides: rows.length, overflowing: rows.filter(r => r.overflow).map(r => r.slide), rows };
})()
