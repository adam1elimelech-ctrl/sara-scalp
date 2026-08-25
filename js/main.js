// Sara Scalp - Main JS

document.addEventListener('DOMContentLoaded', function () {
  // Detect language
  const isHebrew = document.documentElement.lang === 'he' || document.documentElement.dir === 'rtl';

  // Mobile menu
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const nav = document.querySelector('.nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', () => {
      nav.classList.toggle('open');
    });
  }

  // FAQ accordion
  document.querySelectorAll('.faq-question').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.parentElement;
      item.classList.toggle('open');
    });
  });

  // Booking OTP simulation
  const bookingForm = document.getElementById('bookingForm');
  if (bookingForm) {
    let generatedOTP = null;
    const step1 = document.getElementById('step1');
    const step2 = document.getElementById('step2');
    const step3 = document.getElementById('step3');
    const sendOtpBtn = document.getElementById('sendOtpBtn');
    const verifyOtpBtn = document.getElementById('verifyOtpBtn');
    const submitBookingBtn = document.getElementById('submitBookingBtn');
    const otpMessage = document.getElementById('otpMessage');
    const formMessage = document.getElementById('formMessage');

    // Step 1: Send OTP
    if (sendOtpBtn) {
      sendOtpBtn.addEventListener('click', function (e) {
        e.preventDefault();
        const phone = document.getElementById('phone').value.trim();
        const name = document.getElementById('name').value.trim();

        if (!name || name.length < 2) {
          showMsg(otpMessage, 'error', isHebrew ? 'נא להזין שם מלא' : 'Please enter your full name');
          return;
        }
        if (!phone || phone.length < 9) {
          showMsg(otpMessage, 'error', isHebrew ? 'נא להזין מספר טלפון תקין' : 'Please enter a valid phone number');
          return;
        }

        // Generate mock OTP (in production replace with real SMS API call)
        generatedOTP = String(Math.floor(100000 + Math.random() * 900000));
        
        // For demo purposes we show the code. In production remove this line.
        console.log('Demo OTP:', generatedOTP);
        
        showMsg(otpMessage, 'info', isHebrew 
          ? 'קוד אימות נשלח לטלפון שלך. (בדמו: הקוד הוא ' + generatedOTP + ')'
          : 'Verification code sent to your phone. (Demo: the code is ' + generatedOTP + ')');
        
        step1.style.display = 'none';
        step2.classList.add('active');
        document.getElementById('otp').focus();
      });
    }

    // Step 2: Verify OTP
    if (verifyOtpBtn) {
      verifyOtpBtn.addEventListener('click', function (e) {
        e.preventDefault();
        const entered = document.getElementById('otp').value.trim();
        if (entered === generatedOTP) {
          showMsg(otpMessage, 'success', isHebrew ? 'הטלפון אומת בהצלחה!' : 'Phone verified successfully!');
          setTimeout(() => {
            step2.classList.remove('active');
            step3.classList.add('active');
            step3.style.display = 'block';
          }, 800);
        } else {
          showMsg(otpMessage, 'error', isHebrew ? 'קוד שגוי. נסה שוב.' : 'Incorrect code. Please try again.');
        }
      });
    }

    // Step 3: Submit booking request
    if (submitBookingBtn) {
      submitBookingBtn.addEventListener('click', function (e) {
        e.preventDefault();
        const service = document.getElementById('service').value;
        const preferredDate = document.getElementById('preferredDate').value;

        if (!service) {
          showMsg(formMessage, 'error', isHebrew ? 'נא לבחור טיפול' : 'Please select a treatment');
          return;
        }
        if (!preferredDate) {
          showMsg(formMessage, 'error', isHebrew ? 'נא לבחור תאריך מועדף' : 'Please select a preferred date');
          return;
        }

        // In production: send to backend / Acuity / email service
        showMsg(formMessage, 'success', isHebrew 
          ? 'הבקשה לקביעת תור נשלחה בהצלחה! ניצור איתך קשר בהקדם לאישור התור. תודה שבחרת בשרה סקאלפ.'
          : 'Appointment request sent successfully! We will contact you soon to confirm. Thank you for choosing Sara Scalp.');
        
        // Reset form after short delay
        setTimeout(() => {
          bookingForm.reset();
          step1.style.display = 'block';
          step2.classList.remove('active');
          step3.style.display = 'none';
          step3.classList.remove('active');
          formMessage.style.display = 'none';
          otpMessage.style.display = 'none';
          generatedOTP = null;
        }, 5000);
      });
    }
  }

  function showMsg(el, type, text) {
    if (!el) return;
    el.className = 'form-message ' + type;
    el.textContent = text;
    el.style.display = 'block';
  }
});
