
import React, { useRef, useState } from 'react'
import axios from 'axios';
import Spinner from './Spinner';

export default function Feature() {

    const inputRef = useRef()

    const [file,setFile] = useState();
    const [response,setResponse] = useState();
    const [loading,setLoading] = useState(false);

    const handleChange = event => {
        setFile(event.target.files[0])
        
    };
 
    const uploadFile = async () => {

        if (!file){
            alert("Please select a file")
            return 
        }

        setLoading(true);
        setResponse(null);

        const formData = new FormData();
        formData.append(
            "file",
            file
        );

        try {
            const res = await axios.post("http://localhost:8000/upload", formData);
            setResponse("Prediction Response - " + res.data.message)
            
        } catch (error) {
            console.log(error)
            setResponse("An unknown error occured")
        }
        finally{
            setLoading(false);
            setFile(null);
            inputRef.current.value = ""
        }
    };
 
    
    const getFileData = () => {
 
        if (file) {
 
            return (
                <div>
                    <h2>File Details:</h2>
                    <p>File Name: {file.name}</p>
 
                    <p>File Type: {file.type}</p>
 
                    <p>
                        Last Modified:{" "}
                        {file.lastModifiedDate.toDateString()}
                    </p>
 
                </div>
            );
        } else {
            return (
                <></>
            );
        }
    };    
    
  return (
    <section id='feature' className='flex flex-col items-center justify-center gap-12 p-20 pb-[250px]'>
        <h1 className='text-center font-bold text-5xl lg:text-start'>Our AI Service</h1>

        <p className='text-center text-2xl lg:text-start'>Upload your MRI scanned Images here</p>

        <div className='flex flex-col items-center gap-12 lg:flex-row'>
            <input ref={inputRef} type="file" accept="image/png, image/jpg, image/jpeg" onChange={handleChange}/>
            <button className='bg-textBlue text-white font-bold w-32 p-2 rounded-2xl hover:bg-sky-700 ease-in-out duration-500' onClick={uploadFile}>Upload</button>
        </div>
        {getFileData()}
        {loading && <Spinner/>}
        {response && <div className='font-bold text-center text-[30px]'>{response}</div>}
    </section>
  )
}
