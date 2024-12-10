// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

// Create a class named Video. The class should be constructed with the following parameters:
// title (a string)
// uploader (a string, the person who uploaded it)
// time (a number, the duration of the video - in seconds)
// Create a method called watch() which displays a string as follows:
// “uploader parameter watched all time parameter of title parameter!”
class Video {
    constructor(title, uploader, time) {
        this.title = title,
        this.uploader = uploader,
        this.time = time
    };
watch() {
    console.log(`${this.uploader} watched all ${this.time} seconds of "${this.title}"!`)
    };
};

// Instantiate a new Video instance and call the watch() method.
// Instantiate a second Video instance with different values.

const video1 = new Video ("Krusty Show", "Bart", 600);
const video2 = new Video ("Itchy and Scratchy Show", "Liza", 300);

video1.watch();
video2.watch();

// Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)
// Think of the best data structure to save this information within the array.

const videoData = [
    {title: 'Threat Level: Midnight', uploader: 'Michael', time: 3600},
    {title: 'How Paper Is Made', uploader: 'Dwight', time: 2400},
    {title: 'Anger Management', uploader: 'Andy', time: 1800},
    {title: 'Introduction to Flinkerton', uploader: 'Jim', time: 180},
    {title: 'Kevin\'s Famous Chili', uploader: 'Kevin', time: 7200},
];

// Bonus: Loop through the array to instantiate those instances.

const loopThru = videoData.map(video => new Video(video.title, video.uploader, video.time));

loopThru.forEach(video => video.watch());

console.log(loopThru)