// G4 溢出量測：在瀏覽器開啟 deck.html 後執行，回傳每頁是否有內容超出 16:9 版面。
// 只量測，不修改頁面。
(() => {
  const slides = [...document.querySelectorAll("section.slide")];
  // 內容的下緣不可超過頁框扣掉下方留白的位置（否則會壓到頁碼或被裁掉）。
  const rows = slides.map((s, i) => {
    const box = s.getBoundingClientRect();
    const padBottom = parseFloat(getComputedStyle(s).paddingBottom);
    const limit = box.bottom - padBottom;
    const body = s.querySelector(".body");
    const last = body && body.lastElementChild;
    const contentBottom = last ? last.getBoundingClientRect().bottom : box.top;
    const over = contentBottom > limit + 1 || s.scrollHeight > s.clientHeight + 1 || s.scrollWidth > s.clientWidth + 1;
    return { slide: i + 1, id: s.id, overflow: over, spare_px: Math.round(limit - contentBottom), slide_px: Math.round(box.height) };
  });
  return { slides: rows.length, overflowing: rows.filter(r => r.overflow).map(r => r.slide), rows };
})()
