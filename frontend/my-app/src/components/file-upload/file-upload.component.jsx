/**
 * 
 * References:
 *    https://stackoverflow.com/questions/24139216/how-can-i-serialize-an-input-file-object-to-json
 *    // send as formData to backend - https://www.sammeechward.com/uploading-images-express-and-react
 */


import React, { useRef, useState } from "react";
import axios from 'axios'
import {
  FileUploadContainer,
  FormField,
  DragDropText,
  UploadFileBtn,
  FilePreviewContainer,
  ImagePreview,
  PreviewContainer,
  PreviewList,
  FileMetaData,
  RemoveFileIcon,
  InputLabel,
  PalettePreview,
  UL,
  PaletteSlice
} from "./file-upload.styles";

const KILO_BYTES_PER_BYTE = 1000;
const DEFAULT_MAX_FILE_SIZE_IN_BYTES = 500000;

//takes nested object keys and converts to array,returns array
const convertNestedObjectToArray = (nestedObj) =>
  Object.keys(nestedObj).map((key) => nestedObj[key]);
  

const convertBytesToKB = (bytes) => Math.round(bytes / KILO_BYTES_PER_BYTE);

const FileUpload = ({
  label,
  updateFilesCb,
  maxFileSizeInBytes = DEFAULT_MAX_FILE_SIZE_IN_BYTES,
  ...otherProps
}) => {
  const fileInputField = useRef(null);
  const [files, setFiles] = useState({});
  const [colors, setColors] = useState({})

  const handleUploadBtnClick = () => {
    fileInputField.current.click();
  };


  /** Adds uploaded files into state */
  const addNewFiles = (newFiles) => {
    for (let file of newFiles) {
      if (file.size < maxFileSizeInBytes) {
        if (!otherProps.multiple) {
        //   coverting file object to javascript object, and returning as javascript object
            return { file };
        }
        // console.log(file.name)
        files[file.name] = file;
      }
    }
    return { ...files };
  };

  const callUpdateFilesCb = (files) => {
    const filesAsArray = convertNestedObjectToArray(files);
    updateFilesCb(filesAsArray);
    
  };



  /* 
    event.target.files is a filelist object, each item in filelist is a file object
    console.log(e.target.files)
    new object construction, key = files, value = newFiles
    const { files: newFiles } = e.target;
  */
  const handleNewFileUpload = (e) => {
    const newFiles = e.target.files
    // console.log(newFiles[0].name)
    if (newFiles.length) {
      let updatedFiles = addNewFiles(newFiles);
      setFiles(updatedFiles);
      callUpdateFilesCb(updatedFiles);
      
    }
    sendToBack()
  };


  

  /*
  files object in state has the structure
    files = {
      img_1.jpg:File {name: 'img_1.jpg', lastModified: 1635440969159, lastModifiedDate: Thu Oct 28 2021 13:09:29 GMT-0400 (Eastern Daylight Time), webkitRelativePath: '', size: 37949, …}
      img_2.jpg: File {name: 'img_2.jpg', lastModified: 1631824994866, lastModifiedDate: Thu Sep 16 2021 16:43:14 GMT-0400 (Eastern Daylight Time), webkitRelativePath: '', size: 125551, …}
      img_4.jpeg: File {name: 'img_4.jpeg', lastModified: 1668789510322, lastModifiedDate: Fri Nov 18 20}
    }

    where the key is the name of uploaded image
    and File is the literal file object uploaded
    Each uploaded file object has the structure
        File {name: 'img_1.jpg', lastModified: 1635440969159, lastModifiedDate: Thu Oct 28 2021 13:09:29 GMT-0400 (Eastern Daylight Time), webkitRelativePath: '', size: 37949, …}
  
    iterate all entries in files object by key,val pair
    each val (literal file object) is appended to formdata under the same key 'file'
    Then accessed on Flask backend using reqeust.files.getlist('file')
        */
  let temp = []
  const sendToBack= async () =>{

      const formData = new FormData()
      // console.log(files)
      for(const[key,value] of Object.entries(files)){
        // console.log(`${key}:${value}`);
        formData.append('file',value)
      }
      console.log(formData.getAll('file'))
      // output: {img_1.jpg: File, img_2.jpg: File, img_4.jpeg: File}

      // for (const value of formData.values()){
      //   console.log(value)
      //   /* output: 
      //       img_1.jpg:[object File]
      //       img_2.jpg:[object File]
      //       img_4.jpeg:[object File]
      //   */
      // }    
      const result = await axios.post('http://127.0.0.1:5000/upload',formData, {headers: {'Content-Type':'multipart/form-data'}})  
      var img_res = result['data']

      for(var i = 0; i<img_res.length;i++){
        console.log(img_res[i])
      }

      
      // // // send colors to component
      // for(const[key,value] of Object.entries(files)){
      //     setColors(files.fileName:)
      // }
      // console.log(colors)
    }

  const removeFile = (fileName) => {
    delete files[fileName];
    setFiles({ ...files });
    callUpdateFilesCb({ ...files });
  };

  return (
    <>
      <FileUploadContainer>
        <InputLabel>{label}</InputLabel>
        <DragDropText>Drag and drop your files anywhere or</DragDropText>
        <UploadFileBtn type="button" onClick={handleUploadBtnClick}>
          <i className="fas fa-file-upload" />
          <span> Upload {otherProps.multiple ? "files" : "a file"}</span>
        </UploadFileBtn>
        <FormField
          type="file"
          ref={fileInputField}
          onChange={handleNewFileUpload}
          title=""
          value=""
          {...otherProps}
        />
      </FileUploadContainer>
     
     <FilePreviewContainer>
        <span>Images</span>
        <PreviewList>
          {/* this returns list of image elements
          iterating through each file in the files state */}
          {Object.keys(files).map((fileName, index) => {
            // console.log(Object.keys(files))
            // console.log(fileName)
            let file = files[fileName];
            
            let isImageFile = file.type.split("/")[0] === "image";
            return (
              //A “key” is a special string attribute you need to include when creating lists of elements. We’ll discuss why it’s important in the next section.
              <PreviewContainer key={fileName}>
                  <div>
                    
                    <UL>
                      
                      {/* actual image */}
                      {isImageFile && (
                      <ImagePreview
                        src={URL.createObjectURL(file)}
                        alt={`file preview ${index}`}
                      />
                      )}
                      
                      {/* palette for current image */}
                      <PalettePreview >
                        <PaletteSlice>
                          
                        </PaletteSlice>
                      </PalettePreview>
                      
                    </UL>


                    
                    {/* file metadata overlayed on img */}
                    <FileMetaData isImageFile={isImageFile}>
                      <span>{file.name}</span>
                      <aside>
                        <span>{convertBytesToKB(file.size)} kb</span>
                        <RemoveFileIcon
                          className="fas fa-trash-alt"
                          onClick={() => removeFile(fileName)}
                        />
                      </aside>
                      </FileMetaData>
                    
                  </div>
              </PreviewContainer>
              
            );
          })}
        </PreviewList>
      </FilePreviewContainer>
    </>
  );
};

export default FileUpload;




/*

    The default behavior or file input tag is to open file explorer when its clicked
    we want to open file explorer when 'upload files' button is clicked
    to do that we need a DOM reference to the file input tag
          To create a DOM reference, we use the useRef hook
          This hook returns a mutable reference object, where its .current property refers
          to a DOM node. Which will be the file input tag in this case

          useREf hook allows you to persist values between renders
          can be used to store a mutable value that doesnt cause a re-render when updated
          can be used to access a DOM element directly
            useRef() only returns one item - it returns an object called current


    Once the useRef hook is used, we must pass the returned value to the ref attribute of the file input tag
          -> ref={fileInputField}

          const fileInputField = React.useRef(null)

          return (
              <input type="file" ref={fileInputField} />
          )

    PROPS for File-upload.component
            label -> determines labels of the component
            MaxFileSizeinBytes - for limiting file upload size
            updateFilesCb - callback function used for sending 'files' state to parent component

                  why send 'files' state to parent component?
                      typically the file upload component will be used in a form
                      , when working with forms in react, the component stores the form data in the state
                      so for the parent component to also store the uploaded files, we need the file upload component to send it

                  why do we need a callback function to send the files state to the parent component
                      because react has a unidirectional data flow - we cant easily pass data from the child component (file upload component)
                      to the parent component.
                      To workaround this, we pass a function declared in the parent component and the file upload component will call that function
                      with the files state as an argument. 


                          import React from "react"

                          const DEFAULT_MAX_FILE_SIZE_IN_BYTES = 500000;

                          const FileUpload =  ({
                            label,
                            updateFilesCb,
                            maxFileSizeInBytes = DEFAULT_MAX_FILE_SIZE_IN_BYTES,
                            ...otherProps
                          }) => {
                            const fileInputFiled = useRef(null);
                            const[files,setFiles] = useState({})
                          }

                          return (
                            <input type="file" ref={fileInputField}
                          )
                        }




                  take otherProps variable and pass ot the file input tag
                  this is so we can add attributes to the file input tag - from the parent component via props
                          <input
                            type="file"
                            ref={fileInputField}
                            title=""
                            value=""   <- set to "" to get rid of default text that shows up by default when hovering over the input tag "no file chosen"
                            {...otherProps}
                          />
                  
                  also, setting the value attribute to "" fixes an edge case where uploading a file right after
                  removing it does not change the files state
                  The files state only changes once the value of the input tag changes
                  this bug occurs because when we remove a file, the input tags value does not change
                  rince state changes re-render the HTML, setting the value attribute to "" resets the input tags value on each files state change


                  in second part of html, we are iterating through each file in files state
                  and displaying file name, size in kb and image preview if the file type is image

                        to display the iamge preview, we use URL.createObjectURL functino.
                        The create ObjectURL function takes an object - a file object in this case, and returns a temp
                        URL for accessing the file - we then set that URL to src attribute of an img tag
                            The URL lifetime is tied to the document in the window on which it was created.
                            The new object URL represents the specified File object or Blob object

                      
            functions for file state to be modified
                        earlier, we created a DOM reference using the useRef hook
                        Now we're going to open the file explorere when "upload files" is clicked
                        To do that, we use the handleUploadBtnClick function
                        
                          const handleUploadBtnClick = () =>{
                              fileInputField.current.click();
                          }
                   
                          
            otherProps var is being used to add attribted to the file input tag
            if we dont pass a multiple prop to the file upload component - the file input tag DOES NOT allow
            for selecting multiple files
                          if theres a multiple prop, the selected files get added to the files state
                          otherwise selecting a new file will remove the prevous files state and replace it with the newly selected one

            
            callUpdateFilesCb function takes the value returned from addNewFiles
            and converts the files state to an aray - and calls the updateFilesCb function (from the props)
                          why is updatedFiles passed to callUpdateFilesCb when we can just use the files state within the function?
                              because react state updates are async, theres no gurantee that when callUpdateFilesCb gets called - that the files state will have changed

                          

            
                        
                  

*/

