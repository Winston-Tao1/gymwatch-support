'use strict';
for (const button of document.querySelectorAll('[data-copy]')) {
  button.addEventListener('click', async () => {
    const status = document.querySelector('.copy-status');
    const chinese = document.documentElement.lang.startsWith('zh');
    try {
      await navigator.clipboard.writeText(button.dataset.copy);
      status.textContent = chinese ? '已复制 Gym Watch' : 'Copied Gym Watch';
    } catch {
      status.textContent = chinese ? '请手动搜索 Gym Watch / 健身人' : 'Search for Gym Watch / 健身人';
    }
  });
}
