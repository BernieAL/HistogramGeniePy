
// This is a file that explains each piece of code

/*
setFiles is the state modifier for Files state object

*/


// FUNCTIONS
/* 
addNewFiles(newFIles)
    takes newFiles which is filelist object (containing all uploaded file objects) from event e
    for each file object in filelist object
        if file object's size property is less than max allowed bytes    
            if multiple property of otherProps is not true (meaning only single file was uploaded)
                return the single file object as javascript object
            otherwise, 
                store current file in state files with key file.name
                    files[file.name] = file

        lastly return spread of state files, meaning return everything from before plus what was added in the for loop
*/


/* 
handleNewFileUpload
    gets files list object off event and store as newFiles
    if length of fileList object greather than 0
        set updatedFiles to be return of addNewFiles(newFiles)
                addNewFiles returns 
                SEE addNewFiles(newFiles) for more information
        then call setFiles with updatedFiles
                SEE setFiles()
        then calls callUpdateFilesCb() with updatedFiles
                See callUpdateFiles()
*/

/* 


callUpdateFilesCb(updatedFiles)
    takes updateFiles file list object which are most recently updated files
    converts file list object to array of file list objects
    call updateFilesCb() with array
        updateFilesCb prop recieves updateUploadedFiles from parent as prop value

*/



/*
COMPONENTS

    FileUploadContainer
        parent container for all file upload components
        takes no props
    
    PreviewList
        container for all image components
        takes no props
        inside PreviewList
            get all keys from files state object
            each key is the  actually the fileName of a file object
                retrieve file object value from file state object, using fileName as key, assing to file
                check if the file is an imageFile, store bool reslt in isImageFile

            in return of previewList
                render PreviewContainer with key as fileName
            
            PreviewContainer component
                does conditinal render, checks if isImageFile true 
                and if ImagePreview component successfully renders

            ImagePreview component
                src attribute set to URL created for current file object
                alt attribute set to index of file in files object

            FileMetaData has prop isImageFile which is conditional css rendering    
    


*/






