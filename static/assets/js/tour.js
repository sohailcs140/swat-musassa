/**
 * Tour
 */

'use strict';

(function () {

  
  function setupTour(tour) {
    const backBtnClass = 'btn btn-sm btn-outline-secondary md-btn-flat waves-effect',
      nextBtnClass = 'btn btn-sm btn-primary btn-next waves-effect waves-light';
    tour.addStep({
      title: 'Navbar',
      text: 'This is the navigation bar for your website.',
      attachTo: { element: '.navbar', on: 'bottom' },
      buttons: [
        {
          action: tour.cancel,
          classes: backBtnClass,
          text: 'Skip'
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });
    tour.addStep({
      title: 'Search bar',
      text: 'You can navigate to different pages from here.',
      attachTo: { element: '.navbar-nav.align-items-center', on: 'top' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });
    tour.addStep({
      title: 'Theme Customization',
      text: 'You can switch between dark and light modes for your website.',
      attachTo: { element: '.dropdown-style-switcher', on: 'top' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });
    tour.addStep({
      title: 'Quick Access Shortcuts',
      text: 'Use these shortcuts to navigate your website efficiently.',
      attachTo: { element: '.dropdown-shortcuts', on: 'bottom' },
      buttons: [
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });
    tour.addStep({
      title: 'Notifications',
      text: 'Stay updated with real-time alerts and important updates.',
      attachTo: { element: '.dropdown-notifications', on: 'bottom' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });
    tour.addStep({
      title: 'User Account',
      text: 'Manage your profile, settings, and account information here.',
      attachTo: { element: '.dropdown-user', on: 'bottom' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });
    tour.addStep({
      title: 'Sidebar Navigation',
      text: 'Access all your pages and key sections through this sidebar.',
      attachTo: { element: '#layout-menu', on: 'right' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });

    tour.addStep({
      title: 'Dashboard',
      text: 'Get an overview of your key metrics and recent activities here.',
      attachTo: { element: '.dashboard', on: 'right' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });

    tour.addStep({
      title: 'Visas',
      text: `Under the Visas tab, you can access detailed information and management options for:<br>
      <br>
      <ul>
        <li>
          <strong>Visa Type</strong>
          View and manage different types of visas.
        </li>
        <li>
        <strong>Visa Renewal</strong>
        Handle visa renewal processes and track expiration dates.
        </li>
      </ul>
      `,
      attachTo: { element: '.visas', on: 'right' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });


    tour.addStep({
      title: 'Employers',
      text: `Under the Employers section, you can view detailed information and manage records for each employer.
      `,
      attachTo: { element: '.employers', on: 'right' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });

    tour.addStep({
      title: 'Employees',
      text: `Under the Employees section, you can view detailed information and manage records for each employee.
      `,
      attachTo: { element: '.employees', on: 'right' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });

    tour.addStep({
      title: 'User Management',
      text: `Under the Users section, you can add, delete, and update user accounts.
      `,
      attachTo: { element: '.users', on: 'right' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });

    tour.addStep({
      title: 'Recycle Bin',
      text: `Here, you can view and restore deleted items or permanently delete them from the system.`,
      attachTo: { element: '.recycle-bin', on: 'right' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });

    tour.addStep({
      title: 'Tour Completion',
      text: `Thank you for taking the tour! You now have an overview of the main features and navigation of the website. If you have any questions or need further assistance, please reach out directly.`,
      attachTo: { element: '', on: 'center' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'finish',
          classes: nextBtnClass,
          action: tour.cancel
        }
      ]
    });
    return tour;
  }

  

  const is_tour_finish = localStorage.getItem("is_tour_finish")
  
  
  function start_tour() {

    const tourVar = new Shepherd.Tour({
      defaultStepOptions: {
        scrollTo: false,
        cancelIcon: {
          enabled: true
        }
      },
      useModalOverlay: true
    });

    setupTour(tourVar).start();
  }

  // if tour is not finish for first time then call it
  if (!is_tour_finish){

    start_tour()
    localStorage.setItem("is_tour_finish", "true")
  }



  // ! Documentation Tour only
  const startBtnDocs = document.querySelector('#shepherd-docs-example');

  function setupTourDocs(tour) {
    const backBtnClass = 'btn btn-sm btn-label-secondary md-btn-flat waves-effect',
      nextBtnClass = 'btn btn-sm btn-primary btn-next waves-effect waves-light';
    tour.addStep({
      title: 'Navbar',
      text: 'This is your navbar',
      attachTo: { element: '.navbar', on: 'bottom' },
      buttons: [
        {
          action: tour.cancel,
          classes: backBtnClass,
          text: 'Skip'
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });
    tour.addStep({
      title: 'Footer',
      text: 'This is the Footer',
      attachTo: { element: '.footer', on: 'top' },
      buttons: [
        {
          text: 'Skip',
          classes: backBtnClass,
          action: tour.cancel
        },
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Next',
          classes: nextBtnClass,
          action: tour.next
        }
      ]
    });
    tour.addStep({
      title: 'Social Link',
      text: 'Click here share on social media',
      attachTo: { element: '.footer-link', on: 'top' },
      buttons: [
        {
          text: 'Back',
          classes: backBtnClass,
          action: tour.back
        },
        {
          text: 'Finish',
          classes: nextBtnClass,
          action: tour.cancel
        }
      ]
    });

    return tour;
  }

  if (startBtnDocs) {
    // On start tour button click
    startBtnDocs.onclick = function () {
      const tourDocsVar = new Shepherd.Tour({
        defaultStepOptions: {
          scrollTo: false,
          cancelIcon: {
            enabled: true
          }
        },
        useModalOverlay: true
      });

      setupTourDocs(tourDocsVar).start();
    };
  }
})();
