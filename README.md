# GradientFlowDialog: A Custom wxPython Progress Dialog  

GradientFlowDialog is a visually appealing and functional progress dialog created using wxPython. It features a dynamic gradient progress bar, thread-safe updates, and a cancelable operation, making it a perfect example of blending aesthetics with usability in Python GUI development.  

---

## Features  

- **Gradient Progress Bar**: A smooth, visually pleasing gradient effect for progress representation.  
- **Cancelable Operations**: Users can stop long-running tasks with a simple and intuitive cancel button.  
- **Thread-Safe Updates**: The dialog handles progress updates on a separate thread, ensuring the GUI remains responsive.  
- **User-Friendly Design**: A clean and modern interface that integrates seamlessly into wxPython applications.  

---

## Demo  
_A quick preview of the GradientFlowDialog in action._  

![Demo GIF](/demo.gif)  

---

## Installation  
Clone this repository to your local machine:  
```
git clone https://github.com/chetanjain2099/CustomProgressDialog.git
```

## Customization
You can easily customize GradientFlowDialog to suit your application's needs:

- **Gradient Colors**: Update the gradient brushes in the `GradientPanel` class to use custom colors for progress and remaining areas.
- **Dialog Size and Style**: Modify the dialog dimensions and style parameters in the `ProgressDialog` class.
- **Cancel Behavior**: Customize the cancellation logic in the `OnCancel` method of the `ProgressDialog` class.
- **Progress Update Rate**: Adjust the delay or logic in the `doWork` method in the `MainFrame` class for finer control over progress updates.



## Contributing
We welcome contributions to improve GradientFlowDialog! To contribute:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes and push them to your fork.
- Open a pull request for review.


## Feedback
Have suggestions or found a bug? Open an issue. Feedback is always welcome!
