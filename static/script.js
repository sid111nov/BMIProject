
  console.log("JavaScript file loaded!");

  document.addEventListener('DOMContentLoaded', function() {
      const form = document.querySelector('form');
      form.addEventListener('submit', (e) => {
          document.getElementById('result').style.display = 'block';
          // Allow the form to submit by not calling e.preventDefault();
      });
  });
    