var use = '{{ user }}';
alert(`hiii ${use}`);
console.log(use)
    
const toggleBtn = document.getElementById("themeToggle");
toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});