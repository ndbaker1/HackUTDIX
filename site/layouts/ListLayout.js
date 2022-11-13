import { useState } from 'react'
import { DragDropFile } from '@/components/DragnDrop'

/**
 * 
 * @param {*} file File object from file upload
 */
function handleFile(file, setPosts) {
  const reader = new FileReader();
  reader.addEventListener('load', async (event) => {
    const data = event.target.result;

    const classDetails = await (await fetch(
      'http://localhost:5000/search/text',
      {
        body: JSON.stringify({ description: data }),
        headers: { 'Content-Type': 'application/json' },
        method: 'POST',
      }
    )).json()

    setPosts(classDetails['records'].reverse())
  });

  reader.readAsBinaryString(file);
}

export default function ListLayout({ title }) {
  const [searchValue, setSearchValue] = useState('')

  const [posts, setPosts] = useState([])

  function fileUpload(file) {
    handleFile(file, setPosts)
  }

  return (
    <>
      <div className="divide-y divide-gray-200 dark:divide-gray-700">
        <div className="space-y-2 pt-6 pb-8 md:space-y-5">
          <h1 className="text-3xl font-extrabold leading-9 tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl sm:leading-10 md:text-6xl md:leading-14">
            {title}
          </h1>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 50%)', gap: '1rem' }}>
            <div style={{ gridColumn: 1 }}>
              <DragDropFile fileHander={fileUpload}></DragDropFile>
            </div>

            <div style={{ gridColumn: 2 }} className="relative max-w-lg">
              <textarea
                aria-label="Paste post description text"
                type="text"
                onChange={(e) => setSearchValue(e.target.value)}
                placeholder="Paste post description text"
                className="w-full h-full rounded-md border border-gray-300 bg-white px-4 py-2 text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-900 dark:bg-gray-800 dark:text-gray-100"
              />
            </div>
          </div>
        </div>
        <ul>
          {posts.map((frontMatter) => {
            const { course_number, title, description } = frontMatter['class_details']
            const score = frontMatter['score']

            return (
              <li className="py-4">
                <article className="space-y-2 xl:grid xl:grid-cols-4 xl:items-baseline xl:space-y-0">
                  <div className="space-y-3 xl:col-span-3">
                    <details>
                      <summary className="text-2xl font-bold tracking-tight">
                        {course_number} - {title}
                        <div className="prose text-gray-500 dark:text-gray-400">
                          Rating : {score}
                        </div>
                      </summary>
                      <div className="prose max-w-none text-gray-500 dark:text-gray-400 text-sm">
                        {description.substring(description.indexOf(')') + 2)}
                      </div>
                    </details>
                  </div>
                </article>
              </li>
            )
          })}
        </ul>
      </div>
    </>
  )
}
