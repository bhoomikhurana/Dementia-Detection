import React from 'react'


export default function Main() {
  return (
    <main id='main' className='flex py-32 pb-[219px] flex-col-reverse  justify-center items-center bg-customBlue overflow-hidden relative lg:flex-row'>
        <div className='flex flex-col gap-12 w-[80%] z-10 lg:w-[41%]'>
            <div>
                <p className='text-center font-bold text-5xl lg:text-left'>Predict</p>
                <p className='text-center font-bold text-5xl lg:text-left text-textBlue'>Prevent</p>
                <p className='text-center font-bold text-5xl lg:text-left'>Prevail</p>
            </div>

            <div className=' self-center text-center  text-lg lg:text-left lg:self-start lg:w-[80%]'>
                Utilizing advanced artificial intelligence to predict the likelihood of Alzheimer's disease from medical images.
            </div>

            <a className='self-center lg:self-start bg-textBlue text-white font-bold w-32 p-2 rounded-2xl text-center hover:bg-sky-700 ease-in-out duration-500' href='/#feature'>Get Started</a>
        </div>
            
        <div className='z-10'>
            <img className=' h-[300px] w-[300px]' src="/brain.png" alt="" srcSet="" />
        </div>

        <div className="primary-color-border primary-color-[100] absolute -left-56 top-20 h-[400px] w-[400px] rounded-full border-[60px] border-blue-100 "></div>
        <div className="primary-color-border primary-color-[100] absolute -right-56 top-60 h-[400px] w-[400px] rounded-full border-[60px] border-blue-100 "></div>
    </main>
  )
}
